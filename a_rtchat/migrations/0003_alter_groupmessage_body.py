# Generated by Django 5.0.2 on 2024-04-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0002_alter_groupmessage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmessage',
            name='body',
            field=models.CharField(max_length=10000000),
        ),
    ]
