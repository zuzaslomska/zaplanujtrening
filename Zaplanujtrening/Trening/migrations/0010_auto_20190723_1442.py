# Generated by Django 2.1.7 on 2019-07-23 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0009_auto_20190723_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='all_votes',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user_voted',
        ),
        migrations.AddField(
            model_name='myuser',
            name='all_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Ocena'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_com', to=settings.AUTH_USER_MODEL),
        ),
    ]
