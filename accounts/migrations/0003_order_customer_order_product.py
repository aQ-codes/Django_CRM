# Generated by Django 5.0.1 on 2024-02-13 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product_alter_customer_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product'),
        ),
    ]