# Generated by Django 4.0 on 2022-01-13 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripttion',
            new_name='description',
        ),
    ]