"""Zaplanujtrening URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Trening.views import MainSite, Registration, Login, About, Contact,MyAccount,Logout,TrainersView\
    #,EditProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainSite.as_view()),
    path('registration/', Registration.as_view()),
    path('login/', Login.as_view()),
    path('trainers/', TrainersView.as_view()),
    path('about/', About.as_view()),
    path('contact/', Contact.as_view()),
    path('myaccount/', MyAccount.as_view()),
  #  path('myplans/', MyPlans.as_view()),
  #  path('editprofile/<id>', EditProfile.as_view()),
    path('logout/', Logout.as_view()),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
