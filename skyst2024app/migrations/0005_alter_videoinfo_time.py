# Generated by Django 4.2.7 on 2024-03-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyst2024app', '0004_videoinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoinfo',
            name='time',
            field=models.IntegerField(),
        ),
    ]
