# Generated by Django 4.0.4 on 2022-05-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circular',
            name='title',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
