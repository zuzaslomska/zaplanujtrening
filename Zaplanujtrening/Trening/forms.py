from django import forms
from .models import User

class NameForm(model.Form):
    model = User
    exclude = ['login','rating', 'opinion',]