# Generated by Django 2.0.7 on 2018-09-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_user',
        ),
    ]
