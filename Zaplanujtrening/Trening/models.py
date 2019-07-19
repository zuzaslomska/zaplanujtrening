from django.db import models

# Create your models here.

class UserFile(models.Model):
    photo = models.ImageField(upload_to='usersPhoto/%Y/%m/%d/')
