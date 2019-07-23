
from django.views.generic import ListView
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from .forms import RegistrationForm, EditProfileForm
from .models import MyUser,Rating



class MainSite(View):
    def get(self,request):
        return render(request,"index.html")



class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self,form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        email = form.cleaned_data["email"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        about = form.cleaned_data["about"]
        avatar = form.cleaned_data["avatar"]

        new_user = MyUser.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            about=about,
                                            avatar=avatar,)
        return super().form_valid(form)


class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self,form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
      #  login_out = request.POST.get("logout")

        user = authenticate(username=username, password=password)
        login(self.request,user)
        return super().form_valid(form)



class TrainersView(ListView):
    template_name = "Trainers.html"
    queryset = MyUser.objects.filter(trener=True)
    context_object_name = "myuser"
    

class MyAccount(TemplateView):
    template_name = 'my_account.html'


# class MyPlans():
"""class EditProfile(UpdateView):
    queryset = MyUser.objects.get(pk=id)
    fields = ['first_name']
    template_name_suffix = '_update_form'"""

"""class EditProfile(FormView):
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = "/myaccount/"

    def form_valid(self,form):
        email = form.cleaned_data["email"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        about = form.cleaned_data["about"]

        change_user = MyUser.objects.update(email=email,
                                            first_name=first_name,
                                            last_name=last_name,
                                            about=about
                                            )

        return super().form_valid(form)"""

class Logout(View):
    def get(self,request):
        logout(request)
        if MyUser.is_authenticated:
            ctx = {"ops":"Nie udało się wylogować"}
            return render(request,"logout.html",ctx)
        ctx = {"ops":"Wylogowano pomyślnie"}
        return render(request,"logout.html",ctx)

    def post(self,request):
        log_out = request.POST.get("wyloguj")
        if log_out:
            return render(request, "index.html",)

class About(TemplateView):
    template_name = 'about.html'


class Contact(TemplateView):
    template_name = 'contact.html'
    success_url = '/'

    

"""
class Logout(View):
    def get(self, request):
        if MyUser is not None:
            logout(request)
            return redirect('/')
        else:
            return HttpResponse("Nie udało sie wylogować")
            """