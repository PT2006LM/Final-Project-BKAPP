# Generated by Django 3.1.2 on 2020-11-30 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0024_auto_20201127_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='coupon',
        ),
    ]
