# Generated by Django 4.2.1 on 2023-05-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ProductionLine', models.CharField(max_length=255)),
            ],
        ),
    ]
