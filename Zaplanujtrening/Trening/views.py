from django.shortcuts import render
from Zaplanujtrening import urls
from django.http import request
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseForbidden

class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"



class Registration(View):
    def get(self,request):
        form = UserCreationForm()
        ctx = {"form":form}
        return render(request, "registration.html", ctx)

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = User.objects.create_user(username = username, password = password)

        ctx = {"form":form}
        return render(request, "registration.html", ctx)


class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get("login")
        userpassword = request.POST.get("password")
        login_out = request.POST.get("logout")

        user = authenticate(username=username, password=userpassword)
        return HttpResponse("OK")

