# Generated by Django 4.2.5 on 2024-01-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=50, null=True, verbose_name='Описание датчика'),
        ),
    ]
