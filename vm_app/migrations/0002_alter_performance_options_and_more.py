# Generated by Django 4.2.7 on 2023-11-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performance',
            options={'verbose_name': 'Performance', 'verbose_name_plural': 'Performance'},
        ),
        migrations.AlterField(
            model_name='performance',
            name='average_response_time',
            field=models.TimeField(),
        ),
    ]
