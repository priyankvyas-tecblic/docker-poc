# Generated by Django 4.2 on 2023-05-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('qunatity', models.IntegerField(verbose_name='Quantity')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('manufacture_place', models.CharField(max_length=50, verbose_name='Manufacture Place')),
            ],
        ),
    ]
