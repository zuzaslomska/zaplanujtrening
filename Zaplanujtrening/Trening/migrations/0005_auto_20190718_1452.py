# Generated by Django 2.1.7 on 2019-07-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0004_auto_20190718_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
