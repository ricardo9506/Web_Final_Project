# Generated by Django 3.0.6 on 2020-12-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea', '0005_auto_20201221_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='endTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='uploadTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]