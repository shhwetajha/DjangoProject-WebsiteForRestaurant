# Generated by Django 4.1.7 on 2023-02-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Booking',
        ),
    ]