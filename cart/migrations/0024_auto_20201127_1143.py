# Generated by Django 3.1.2 on 2020-11-27 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_auto_20201127_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cart',
            new_name='cart_parent',
        ),
    ]
