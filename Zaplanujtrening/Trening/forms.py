from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser,Plans, Parts, Exercises, ExercisesPlans


RATING = [("1","1"),("2","2")
        ,("3","3"),("4","4"),("5","5")]

    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username","password1","password2","email","first_name","last_name","about","avatar")
        labels = {"username":"Nazwa użytkownika",
                  "password1":"Hasło",
                  "password2":"Powtórz hasło",
                  "first_name":"Imię",
                  "last_name":"Nazwisko",
                  "email":"E-mail",
                  "about":"O mnie",
                  "avatar":"Zdjęcie"}


class EditProfileForm(UserChangeForm):
    class Meta:
        model=MyUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'about'
        )

class ContactForm(forms.Form):
    contact_user  = forms.CharField(max_length=120,label="Imię")
    email = forms.EmailField(required=True, label="E-mail")
    message = forms.CharField(widget=forms.Textarea)


class VoteForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING)
    class Meta:
        model = MyUser
        fields = ["rating"]

class PlanForm(forms.ModelForm):

    class Meta:
        model = ExercisesPlans
        fields = '__all__'