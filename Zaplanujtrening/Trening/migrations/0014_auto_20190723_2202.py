# Generated by Django 2.1.7 on 2019-07-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trening', '0013_auto_20190723_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]