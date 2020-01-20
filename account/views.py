#! /usr/bin/env python3
# coding: UTF-8

""" Account views :
access_account, my_account, create_account """


# Imports
import re
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login
from account.forms import Account


def access_account(request):
    """ access_account view :
    connects the user if the information given is correct
    else, display an error message """

    # add Account form in the context
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        # GET THE USER'S DATA AND VERIFY THAT THE ACCOUNT EXISTS
        form = Account(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        # USER'S CONNECTION AND
        # DISPLAY A CONFIRMATION MESSAGE ON THE INDEX PAGE
        # if user exists
        if user:
            login(request, user)
            mail = request.user.email
            context = {'message': "Bonjour {} ! Vous êtes bien connecté.".format(mail)}
            return render(request, 'food/index.html', context)

        # DISPLAY AN ERROR MESSAGE ON THE ACCESS_ACCOUNT PAGE
        # if user does not exists
        if form.is_valid() is False:
            error_list = []
            for key, value in form.errors.as_data().items():
                message = str(key).title() + ' : ' + str(value[0]).\
                          replace("['", "").replace("']", "")
                error_list.append(message)
                context["message"] = error_list
                context["color"] = "red"
        else:
            context["message"] = ["Ce compte n'existe pas."]
            context["color"] = "red"
        return render(request, 'account/access_account.html', context)

    return render(request, 'account/access_account.html', context)


def my_account(request):
    """ my_account view :
    display the user's data on the my_account page """

    mail = request.user.email
    date = request.user.date_joined
    context = {'date': date, 'mail': mail}
    return render(request, 'account/my_account.html', context)



def create_account(request):
    """ create_account view :
        created the user's account if the information given is correct
        else, display an error message on the create_account page """

    # add Account form in the context
    user = get_user_model()
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        # GET THE USER'S DATA
        form = Account(request.POST)
        email = request.POST.get('email')
        password_control = request.POST.get('passwordControl')
        password = request.POST.get('password')

        if form.is_valid() is True:
            # DISPLAY AN ERROR MESSAGE ON THE CREATE_ACCOUNT PAGE
            # if the email isn't valid
            regex = r"^[a-z0-9-_.]+@[a-z0-9-]+\.(com|fr)$"
            result = re.match(regex, email)
            if result is None:
                # create error message
                context["message"] = ["Votre adresse e-mail n'est pas valide."]
                context["color"] = "red"

            # CREATE THE USER'S ACCOUNT AND
            # DISPLAY A CONFIRMATION MESSAGE ON THE INDEX PAGE
            # if the data entered by the user is valid
            else:
                if password_control == password:
                    user.objects.create_user(username='Null', email=email, password=password)
                    context = {"message": "Le compte {} a bien été créé.".format(email)}
                    return render(request, 'food/index.html', context)

                # DISPLAY AN ERROR MESSAGE ON THE CREATE_ACCOUNT PAGE
                # if password and password control aren't the same
                context["message"] = ["Vos mots de passe ne sont pas identiques."]
                context["color"] = "red"

        # DISPLAY AN ERROR MESSAGE ON THE CREATE_ACCOUNT PAGE
        # if the form isn't valid
        else:
            error_list = []
            for key, value in form.errors.as_data().items():
                message = str(key).title() + ' : ' + str(value[0]).\
                          replace("['", "").replace("']", "")
                error_list.append(message)
                context["message"] = error_list
                context["color"] = "red"

    return render(request, 'account/create_account.html', context)
