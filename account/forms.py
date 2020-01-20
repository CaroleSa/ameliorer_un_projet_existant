#! /usr/bin/env python3
# coding: UTF-8

""" ModelForm """


# Imports
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth import get_user_model


class Account(ModelForm):
    """ ModelForm Account
    model : custom User
    fields : email and password """
    class Meta:
        """ Meta class """
        model = get_user_model()
        fields = ["email", "password"]
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Adresse E-mail'}),
            'password': TextInput(attrs={'class': 'form-control',
                                         'Placeholder': 'Mot de passe à 8 caractères',
                                         'type': 'password', 'maxlength': '8', 'minlength':"8"})
        }
