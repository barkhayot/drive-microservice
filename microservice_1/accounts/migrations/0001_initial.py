# Generated by Django 4.1.5 on 2023-01-02 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email Address')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Featured_Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(max_length=255, verbose_name='Comment for Music')),
            ],
        ),
        migrations.CreateModel(
            name='Featured_Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets', models.CharField(max_length=255, verbose_name='Comment for Pets')),
            ],
        ),
        migrations.CreateModel(
            name='Featured_Smoking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoking', models.CharField(max_length=255, verbose_name='Comment for Smoking')),
            ],
        ),
        migrations.CreateModel(
            name='Featured_Talking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talking', models.CharField(max_length=255, verbose_name='Comment for Talking')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('experience', models.IntegerField(blank=True, null=True, verbose_name='Experience of driving')),
                ('over_drive', models.IntegerField(blank=True, null=True, verbose_name='Over Drive')),
                ('address_line', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address Line')),
                ('city', models.CharField(blank=True, max_length=20, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=20, null=True, verbose_name='Country')),
                ('music', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userprofile', to='accounts.featured_music')),
                ('pets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userprofile', to='accounts.featured_pets')),
                ('smoking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userprofile', to='accounts.featured_smoking')),
                ('talking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userprofile', to='accounts.featured_talking')),
            ],
        ),
    ]
