# Generated by Django 4.2.1 on 2023-06-19 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_dailyproductionouput_wok_hr'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionline',
            name='daily_target',
            field=models.PositiveIntegerField(default=0),
        ),
    ]