# Generated by Django 2.1.2 on 2018-10-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_usuario_permissao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usuario_permissao',
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_administrativo',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_entrega',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_padrao',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_secretario',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]