from django.shortcuts import render
from Zaplanujtrening import urls
from django.http import request
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseForbidden


class MainSite(View):
    def get(self,request):
        return render(request,"index.html")

class Registration(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self,form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        new_user = User.objects.create_user(username = username, password = password)
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

