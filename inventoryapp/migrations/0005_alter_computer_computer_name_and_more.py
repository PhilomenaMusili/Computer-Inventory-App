# Generated by Django 5.0.1 on 2024-01-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0004_alter_computer_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
