# Generated by Django 4.2.7 on 2024-03-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyst2024app', '0009_alter_videoinfo_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='videos',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
