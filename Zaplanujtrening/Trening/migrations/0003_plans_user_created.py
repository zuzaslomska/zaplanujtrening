# Generated by Django 2.1.7 on 2019-07-27 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0002_auto_20190726_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='user_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]