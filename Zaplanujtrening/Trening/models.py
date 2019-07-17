from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User,AbstractUser


class Rating(models.Model):
   comments = models.TextField(verbose_name=_("komentarz"))
   rating = models.IntegerField(verbose_name=_("Ocena"))
   all_votes = models.IntegerField()
   opinions = models.ForeignKey(User,on_delete=models.CASCADE)