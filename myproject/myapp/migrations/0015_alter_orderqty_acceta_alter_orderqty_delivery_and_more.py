# Generated by Django 4.2.1 on 2023-05-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_orderqty_acceta_alter_orderqty_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderqty',
            name='accETA',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderqty',
            name='delivery',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderqty',
            name='fabricETA',
            field=models.DateField(blank=True, null=True),
        ),
    ]
