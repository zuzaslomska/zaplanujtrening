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
from Trening.Ready import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from Trening.views import (MainSite, Registration, Login, About, Contact,MyAccount,TrainersView, TrainerDetails,\
    TrainerRegistration, EditProfile, CreatePlan, PlanName, PlanList, PlanDetails, ExercisesList, ExercisesDetails)


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', MainSite.as_view()),
    path('registration/', Registration.as_view()),
    path('registration/trainer',TrainerRegistration.as_view()),
    path('login/', Login.as_view()),
    path('trainers/', TrainersView.as_view()),
    path('trainer/<int:pk>', TrainerDetails.as_view()),
    path('about/', About.as_view()),
    path('contact/', Contact.as_view()),
    path('myaccount/', MyAccount.as_view()),
    path('reset-password/', PasswordResetView.as_view()),
    path('reset-password/done', PasswordResetDoneView.as_view()),
    re_path(r'^reset-password/confirm/<uidb64>/<token>/',
             PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('changepassword/', PasswordChangeView.as_view()),
    path('changepassword/done', PasswordChangeDoneView.as_view()),
    path('editprofile/', EditProfile.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
    path('create/plan/',CreatePlan.as_view()),
    path('name/plan', PlanName.as_view()),
    path('plan/list', PlanList.as_view()),
    path('plan/details/<int:pk>', PlanDetails.as_view()),
    path('exercises/list', ExercisesList.as_view()),
    path('exercises/details/<int:pk>', ExercisesDetails.as_view()),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
