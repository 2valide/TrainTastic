# Generated by Django 4.2.11 on 2024-03-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='datetime',
            field=models.CharField(max_length=100),
        ),
    ]
