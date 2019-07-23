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
