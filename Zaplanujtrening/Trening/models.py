from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,AbstractUser

class MyUser(AbstractUser):
    about = models.TextField()
    trener = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='profile_pics',null=True)
    rating = models.DecimalField(verbose_name=_("Ocena"),default=0,decimal_places=1,max_digits=2)
    all_votes = models.IntegerField(default=0)
    sum_of_votes = models.IntegerField(default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Rating(models.Model):
    comments = models.TextField(verbose_name=_("komentarz"))
    user_comment = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True ,related_name="user_com")


class Parts(models.Model):
    part = models.CharField(max_length=70)


class Exercises(models.Model):
    exercise_name = models.CharField(max_length=70)
    description = models.TextField()
    gif = models.FileField()
    part = models.ForeignKey(Parts, on_delete=models.DO_NOTHING)


class Plans(models.Model):
    plan_name = models.CharField(max_length=70)
    times = models.SmallIntegerField()
    clock = models.TimeField()
    rest_time = models.TimeField()
    exercise = models.ManyToManyField(Exercises, through='ExercisesPlans')


class ExercisesPlans(models.Model):
    exercises = models.ForeignKey(Exercises, on_delete=models.DO_NOTHING)
    plans = models.ForeignKey(Plans, on_delete=models.DO_NOTHING)


