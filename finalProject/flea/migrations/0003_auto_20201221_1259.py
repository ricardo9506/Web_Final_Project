# Generated by Django 3.0.6 on 2020-12-21 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flea', '0002_auto_20201220_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pictureName',
            new_name='picture',
        ),
    ]
