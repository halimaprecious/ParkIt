# Generated by Django 4.0.5 on 2022-06-22 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0003_remove_parkslot_booked_remove_parkslot_booked_slot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkslot',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parkapp.profile'),
        ),
    ]