# Generated by Django 2.0.7 on 2018-09-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180914_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='secretaria_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='secretaria.Secretaria'),
        ),
    ]
