# Generated by Django 5.0.6 on 2024-08-24 12:42

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('home_town', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('status', models.CharField(default='active', max_length=20)),
                ('deactivation_reason', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.usertype')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=355)),
                ('image', models.ImageField(upload_to='folio/')),
                ('category', models.CharField(max_length=100)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.amount')),
                ('designer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('consultation_status', models.CharField(max_length=100)),
                ('proposal', models.CharField(max_length=100)),
                ('schedule_date_time', models.DateTimeField(blank=True, null=True)),
                ('room_type', models.CharField(max_length=100)),
                ('room_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('room_width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('room_height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('design_preferences', models.TextField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_consultations', to=settings.AUTH_USER_MODEL)),
                ('designer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_consultations', to=settings.AUTH_USER_MODEL)),
                ('design_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.design')),
                ('feedback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.feedback')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.amount')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
