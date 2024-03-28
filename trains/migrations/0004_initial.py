# Generated by Django 4.2.11 on 2024-03-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0003_delete_trains'),
    ]

    operations = [
        migrations.CreateModel(
            name='trains',
            fields=[
                ('trainId', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]