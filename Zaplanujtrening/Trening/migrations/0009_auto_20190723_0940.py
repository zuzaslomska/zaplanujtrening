# Generated by Django 2.1.7 on 2019-07-23 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0008_auto_20190722_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='vote',
        ),
        migrations.AddField(
            model_name='rating',
            name='user_voted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]