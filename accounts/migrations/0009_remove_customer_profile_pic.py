# Generated by Django 5.0.1 on 2024-05-05 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]