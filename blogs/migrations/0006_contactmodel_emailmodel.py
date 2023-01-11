# Generated by Django 4.1.1 on 2022-10-21 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80, validators=[django.core.validators.EmailValidator])),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80, validators=[django.core.validators.EmailValidator])),
            ],
        ),
    ]