# Generated by Django 4.0.2 on 2022-02-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_connection_alive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='user',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]