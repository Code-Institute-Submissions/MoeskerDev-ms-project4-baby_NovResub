# Generated by Django 3.2.7 on 2021-11-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
