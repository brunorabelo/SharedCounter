# Generated by Django 4.0.2 on 2022-02-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_connection_connected'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='alive',
            field=models.BooleanField(default=True),
        ),
    ]