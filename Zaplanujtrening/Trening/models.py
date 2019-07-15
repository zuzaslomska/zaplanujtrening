from django.db import models

class PersonalTrainer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    experience = models.TextField()


class Dietician(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    experience = models.TextField()