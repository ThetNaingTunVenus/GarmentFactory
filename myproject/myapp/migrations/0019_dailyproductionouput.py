# Generated by Django 4.2.1 on 2023-06-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_productioninput_daily_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyProductionOuput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('input_qty', models.PositiveIntegerField(default=0)),
                ('cmp_amount', models.FloatField(default=0.0)),
                ('daily_target', models.PositiveIntegerField(default=0)),
                ('shift_1', models.PositiveIntegerField(default=0)),
                ('shift_2', models.PositiveIntegerField(default=0)),
                ('shift_3', models.PositiveIntegerField(default=0)),
                ('shift_4', models.PositiveIntegerField(default=0)),
                ('shift_5', models.PositiveIntegerField(default=0)),
                ('shift_6', models.PositiveIntegerField(default=0)),
                ('shift_7', models.PositiveIntegerField(default=0)),
                ('shift_8', models.PositiveIntegerField(default=0)),
                ('shift_9', models.PositiveIntegerField(default=0)),
                ('shift_10', models.PositiveIntegerField(default=0)),
                ('shift_11', models.PositiveIntegerField(default=0)),
                ('shift_12', models.PositiveIntegerField(default=0)),
                ('total_output_qty', models.PositiveIntegerField(default=0)),
                ('menpower', models.PositiveIntegerField(default=0)),
                ('cmp_pr_menpower', models.FloatField(default=0.0)),
                ('acc_total_cmp', models.FloatField(default=0.0)),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]