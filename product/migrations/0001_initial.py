# Generated by Django 4.1.7 on 2023-02-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=20)),
                ('MOBILENO', models.IntegerField()),
                ('EMAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('NUMBER_OF_GUESTS', models.IntegerField()),
                ('DATE', models.DateField(blank=True, null=True)),
                ('TIME', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
