# Generated by Django 2.2.4 on 2019-08-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20190817_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='admin_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]