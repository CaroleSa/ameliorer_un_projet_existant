#! /usr/bin/env python3
# coding: UTF-8

""" Food views :
index, result, detail, favorites, mentions_legal """


# imports
from django.shortcuts import render
from django.contrib.auth import logout, get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from requests.exceptions import ConnectionError
from food.classes import database
from food.models import Food
from account.forms import Account


def index(request):
    """ index view :
    insert data in the database if database is empty,
    logout the user and display the index page (home) """

    # USER'S DISCONNECTION AND DISPLAY THE INDEX PAGE
    # if the user clicks on the logout logo
    if request.method == 'POST':
        disconnection = request.POST.get('disconnection', 'False')
        if request.user.is_authenticated and disconnection == 'True':
            logout(request)
            context = {'message': "Vous êtes déconnecté."}
            return render(request, 'food/index.html', context)

    # INSERT DATA IF THE DATABASE IS EMPTY
    # DISPLAY THE INDEX PAGE
    try:
        bdd = database.Database()
        bdd.insert_data()
        return render(request, 'food/index.html')
    except ConnectionError:
        context = {'message': "Problème de connexion"}
        return render(request, 'food/index.html', context)


def result(request):
    """ result view :
    display the food data in the result page,
    if there is no result
    display an error message in the index page,
    add id of the favorites food in the context because
    if the user has already registered the food,
    we will not display the floppy logo,
    save the food selected by the user """

    if request.method == 'POST':
        # SAVE FOOD SELECTED BY THE USER
        # if user is authenticated
        save_id_food = request.POST.get('id', None)
        if save_id_food and request.user.is_authenticated:
            id_user = request.user.id
            food = Food.objects.get(id=save_id_food)
            user = get_user_model()
            user = user.objects.get(id=id_user)
            food.favorites.add(user)

        if save_id_food is None:
            # get the name food searched
            food = request.POST.get('search')
            request.session['food'] = food

            # DISPLAY THE INDEX PAGE WITH AN ERROR MESSAGE
            # if there is no food searched
            if not food:
                context = {'message': "Vous n'avez rien demandé"}
                return render(request, 'food/index.html', context)

            context = {'search': food}

            # get the categorie of the food searched
            re_food = '^.*'+food+'.*$'
            re_food = re_food.replace(' ', '.*')
            re_food = r'{}'.format(re_food)
            name = Food.objects.filter(name__iregex=re_food)[:1]
            categorie_food = name.values_list('categorie')

            # DISPLAY THE RESULT PAGE
            # DISPLAY THE RESULT ON PAGE 1
            # if there is food searched
            # and if the categorie exists
            if categorie_food:

                # get data of all foods of the same categorie
                # ordered by nutrition grade
                categorie_food = categorie_food[0]
                data = Food.objects.filter(categorie=categorie_food)
                foods_data = data.order_by('nutrition_grade')

                # use paginator :
                # display of page 1 of result
                paginator = Paginator(foods_data, 18, orphans=4)
                page = request.GET.get('page')
                try:
                    foods_data = paginator.get_page(page)
                except PageNotAnInteger:
                    foods_data = paginator.page(1)
                except EmptyPage:
                    foods_data = paginator.page(paginator.num_pages)
                context['foods_data'] = foods_data

                # DOES NOT DISPLAY THE FLOPPY LOGO
                # if the user has already registered the food
                if request.user.is_authenticated:
                    # get the favorites foods id
                    user = get_user_model()
                    favorites_id = []
                    id_user = request.user.id
                    for elt in user(id=id_user).food_set.values_list('id'):
                        favorites_id.append(elt[0])
                    context['favorites_id'] = favorites_id
                else:
                    context['favorites_id'] = []

                return render(request, 'food/result.html', context)

            # DISPLAY THE INDEX PAGE WITH AN ERROR MESSAGE
            # if there is food searched
            # but that the categorie don't exists
            else:
                context = {"message": "Pas de résultat pour l'aliment {}.".format(food)}
                return render(request, 'food/index.html', context)

    # DISPLAY THE RESULT PAGE
    # DISPLAY THE RESULT ON SEVERAL PAGES : page > 1
    if 'food' in request.session:
        food = request.session['food']
        context = {'search': food}

        # get data of all foods of the same categorie
        list_food = food.split()
        for word in list_food:
            name = Food.objects.filter(name__icontains=word)[:1]
            categorie_food = name.values_list('categorie')
            categorie_food = categorie_food[0]
            data = Food.objects.filter(categorie=categorie_food)
            foods_data = data.order_by('nutrition_grade')

            # use paginator :
            # display of pages > 1 of result
            paginator = Paginator(foods_data, 18, orphans=4)
            page = request.GET.get('page')
            try:
                foods_data = paginator.get_page(page)
            except PageNotAnInteger:
                foods_data = paginator.page(1)
            except EmptyPage:
                foods_data = paginator.page(paginator.num_pages)
            context['foods_data'] = foods_data

            # DOES NOT DISPLAY THE FLOPPY LOGO
            # if the user has already registered the food
            if request.user.is_authenticated:
                # get the favorites foods id
                user = get_user_model()
                favorites_id = []
                id_user = request.user.id
                for elt in user(id=id_user).food_set.values_list('id'):
                    favorites_id.append(elt[0])
                context['favorites_id'] = favorites_id
            else:
                context['favorites_id'] = []

        return render(request, 'food/result.html', context)


def detail(request):
    """ detail view :
    get the data of the food selected by the user
    and display the detail page """

    # DISPLAY THE DETAIL PAGE
    # get id of the food selected
    id_food = request.POST.get('id_food', None)

    # get the data of the food selected
    food = Food.objects.values_list('name', 'nutrition_grade', 'url_picture',
                                    'link', 'energy', 'proteins', 'fat',
                                    'carbohydrates', 'sugars', 'fiber', 'sodium')
    food_data = food.get(id=id_food)
    context = {}
    name_data = ('name', 'nutrition_grade', 'url_picture', 'link', 'energy', 'proteins', 'fat',
                 'carbohydrates', 'sugars', 'fiber', 'sodium')
    for i, elt in enumerate(name_data):
        context[elt] = food_data[i]

    return render(request, 'food/detail.html', context)


def favorites(request):
    """ favorites view :
        get the favorites food data of the user
        and display the favorites page,
        delete the favorite food selected by the user """

    # DELETE THE FOOD SELECTED BY THE USER
    if request.method == 'POST' and request.user.is_authenticated:
        id_food = request.POST.get('id', None)
        id_user = request.user.id
        food = Food.objects.get(id=id_food)
        user = get_user_model()
        user = user.objects.get(id=id_user)
        food.favorites.remove(user)

    # RETURN TO THE ACCESS_ACCOUNT PAGE
    # if user is not authenticated
    if not request.user.is_authenticated:
        form = Account()
        message = ["Veuillez vous connecter pour accéder à vos favoris."]
        context = {'form': form, 'message': message, 'color': 'red'}
        return render(request, 'account/access_account.html', context)

    # DISPLAY THE FAVORITES PAGE
    # if user is authenticated
    # get the favorites food data
    user = get_user_model()
    id_user = request.user.id
    data = user(id=id_user).food_set.all()
    context = {'data': data}

    return render(request, 'food/favorites.html', context)


def mentions_legal(request):
    """ mentions_legal view :
    display the mentions_legal page """
    return render(request, 'food/mentions_legal.html')
