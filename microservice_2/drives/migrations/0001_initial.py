# Generated by Django 4.1.5 on 2023-01-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.IntegerField()),
                ('leaving_city', models.CharField(max_length=255, verbose_name='Leaving City')),
                ('going_city', models.CharField(max_length=255, verbose_name='Going City')),
                ('date', models.DateField()),
                ('leaving_time', models.TimeField()),
                ('coming_time', models.TimeField()),
                ('passengers', models.IntegerField()),
                ('price', models.CharField(default='Free', max_length=50)),
                ('car', models.CharField(max_length=255, verbose_name='Model of Car')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
    ]
