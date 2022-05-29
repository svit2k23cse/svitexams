# Generated by Django 4.0.4 on 2022-05-29 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staffdetails_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.facultydept'),
        ),
    ]
