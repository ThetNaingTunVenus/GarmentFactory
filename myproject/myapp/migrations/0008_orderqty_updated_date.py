# Generated by Django 4.2.1 on 2023-05-15 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_style_buyername'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderqty',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
