from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,AbstractUser
from Zaplanujtrening import settings


class MyUser(AbstractUser):
    about = models.TextField()
    trener = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Rating(models.Model):
    comments = models.TextField(verbose_name=_("komentarz"))
    rating = models.IntegerField(verbose_name=_("Ocena"))
    all_votes = models.IntegerField()
    User_name = models.ForeignKey(MyUser,on_delete=models.CASCADE)
