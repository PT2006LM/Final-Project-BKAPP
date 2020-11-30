# Generated by Django 3.1.2 on 2020-11-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0008_auto_20201119_1015'),
        ('cart', '0005_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodstore.product')),
            ],
        ),
    ]