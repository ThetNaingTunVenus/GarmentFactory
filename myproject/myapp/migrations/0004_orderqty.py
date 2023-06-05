# Generated by Django 4.2.1 on 2023-05-13 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_style_buyer_style_barcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderQty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmp_amount', models.FloatField()),
                ('order_qty', models.PositiveIntegerField(default=0)),
                ('Date', models.DateField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.buyer')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.style')),
            ],
        ),
    ]
