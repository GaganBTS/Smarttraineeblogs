# Generated by Django 4.1.2 on 2022-11-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
