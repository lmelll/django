# Generated by Django 2.2.3 on 2019-07-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190729_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='text',
            field=models.CharField(default=' ', max_length=1024),
        ),
    ]