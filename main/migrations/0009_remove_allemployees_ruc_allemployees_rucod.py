# Generated by Django 4.1.3 on 2022-12-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_allemployees_ruc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allemployees',
            name='ruc',
        ),
        migrations.AddField(
            model_name='allemployees',
            name='rucod',
            field=models.ManyToManyField(to='main.allemployees'),
        ),
    ]