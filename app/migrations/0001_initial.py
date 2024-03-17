# Generated by Django 5.0.3 on 2024-03-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
