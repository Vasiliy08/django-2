# Generated by Django 4.1.3 on 2022-12-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_allemployees_ruc'),
    ]

    operations = [
        migrations.AddField(
            model_name='allemployees',
            name='ruc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]