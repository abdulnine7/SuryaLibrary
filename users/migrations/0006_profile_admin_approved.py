# Generated by Django 2.2.4 on 2019-08-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190816_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
