# Generated by Django 4.2.1 on 2023-06-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_productioninput_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productioninput',
            name='daily_target',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
