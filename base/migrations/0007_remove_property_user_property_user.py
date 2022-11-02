# Generated by Django 4.1.2 on 2022-11-01 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_transaction_item_type_transaction_itemtype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]