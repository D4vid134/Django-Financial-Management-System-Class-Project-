# Generated by Django 4.1.2 on 2022-11-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_property_user_property_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]