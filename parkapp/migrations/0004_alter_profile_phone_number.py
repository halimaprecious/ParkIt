# Generated by Django 4.0.5 on 2022-06-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
