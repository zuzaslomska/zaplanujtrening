from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseForbidden
from .forms import RegistrationForm
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

