# Generated by Django 5.0.1 on 2024-01-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0006_computer_operating_system_alter_computer_ip_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='computer',
            name='operating_system',
        ),
        migrations.AddField(
            model_name='computer',
            name='operating_system',
            field=models.ManyToManyField(blank=True, null=True, to='inventoryapp.operatingsystem'),
        ),
    ]
