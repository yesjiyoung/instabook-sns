# Generated by Django 2.1.8 on 2019-07-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_sns_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sns',
            name='img',
            field=models.TextField(default=''),
        ),
    ]