# Generated by Django 2.2.4 on 2019-08-14 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190814_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='days',
            new_name='day',
        ),
    ]
