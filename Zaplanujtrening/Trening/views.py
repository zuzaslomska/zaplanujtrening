from django.core.mail import send_mail
from django.views.generic import ListView
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView, DetailView
from .forms import RegistrationForm, EditProfileForm, ContactForm, VoteForm, PlanForm, PlanNameForm
from .models import MyUser,Rating, Plans, Parts, Exercises, ExercisesPlans
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class MainSite(View):
    def get(self,request):
        return render(request,"index.html")



class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self,form):
        form.save()

        return super().form_valid(form)


class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/myaccount/'

    def form_valid(self,form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)
        login(self.request,user)
        return super().form_valid(form)


class TrainersView(ListView):
    queryset = MyUser.objects.filter(trener=True)
    template_name = "Trainers.html"
    context_object_name = "myuser"

class MyAccount(TemplateView):
    template_name = 'my_account.html'


# class MyPlans():

class EditProfile(LoginRequiredMixin,UpdateView):
    model = MyUser
    fields = ['username','first_name','last_name','email','avatar','about']
    template_name = 'edit_profile.html'
    success_url = '/myaccount/'


class CreatePlan(LoginRequiredMixin,CreateView):
    model = ExercisesPlans
    form_class = PlanForm
    template_name = 'create_plan.html'
    success_url = '/create/plan'



class About(TemplateView):
    template_name = 'about.html'


class Contact(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact"

    def form_valid(self, form):

        send_mail(
            form.cleaned_data["email"],
            "Wiadomość od "+form.cleaned_data["contact_user"]+": "+form.cleaned_data["message"],
            "dudixxx100@gmail.com",
            ['tomizuz123@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)

class TrainerDetails(View):
    def get(self,request,pk):
        model = MyUser.objects.get(pk=pk)
        comment_model = Rating.objects.filter(user_comment=pk)
        ctx = {"myuser":model,"comment":comment_model}

        return render(request, "Trainer_detail.html", ctx)

    def post(self,request,pk):
        model = MyUser.objects.get(pk=pk)
        comment_model = Rating.objects.filter(user_comment=pk)
        ctx = {"myuser": model,"comment":comment_model}

        vote = request.POST.get("vote")
        model.sum_of_votes += (int(vote))
        model.all_votes += 1
        avg_votes = model.sum_of_votes/model.all_votes
        model.rating = avg_votes
        model.save()
        return render(request, "Trainer_detail.html", ctx)

class TrainerRegistration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        send_mail(
            form.cleaned_data["email"],
            "Wiadomość od "+form.cleaned_data["username"]+": "+"CHCĘ ZOSTAĆ TRENEREM",
            "dudixxx100@gmail.com",
            ["tomizuz123@gmail.com"],
            fail_silently=False,
        )
        send_mail(
            "Zaplanuj Trening",
            "Witaj "+form.cleaned_data['username']+"!"+ "Twoje zapytanie o zostanie trenerem jest rozpatrywane,"
                                                            "poczekaj na wiadomość od nas!" ,
            "dudixxx100@gmail.com",
            [form.cleaned_data["email"]],
            fail_silently=False,
        )
        return super().form_valid(form)


class PlanName(CreateView):
    model = Plans
    form_class = PlanNameForm
    template_name = 'plan_name.html'
    success_url = '/create/plan/'


class PlanList(ListView):
    queryset = Plans.objects.all()
    template_name = 'my_plans.html'
    context_object_name = 'myplan'


class PlanDetails(DetailView):
    model = Plans
    template_name = 'plan_details.html'
 #   slug_url_kwarg = ExercisesPlans.plan


class ExercisesList(ListView):
    queryset = Exercises.objects.all()
    template_name = 'exercises.html'
    context_object_name = 'exercises'
