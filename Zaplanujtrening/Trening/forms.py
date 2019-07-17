from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username","password1","password2","email","first_name","last_name","about")
        labels = {"username":"Nazwa użytkownika",
                  "password1":"Hasło",
                  "password2":"Powtórz hasło",
                  "first_name":"Imię",
                  "last_name":"Nazwisko",
                  "email":"E-mail",
                  "about":"O mnie"}