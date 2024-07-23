# Generated by Django 5.0.6 on 2024-07-06 03:31

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users_delete_customer'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('designer', 'Designer'), ('customer', 'Customer'), ('admin', 'Admin')], max_length=10),
        ),
    ]
