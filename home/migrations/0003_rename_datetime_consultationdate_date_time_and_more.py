# Generated by Django 5.0.6 on 2024-08-30 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_payment_type_remove_consultation_room_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultationdate',
            old_name='datetime',
            new_name='date_time',
        ),
        migrations.AlterUniqueTogether(
            name='consultationdate',
            unique_together={('designer', 'date_time')},
        ),
    ]
