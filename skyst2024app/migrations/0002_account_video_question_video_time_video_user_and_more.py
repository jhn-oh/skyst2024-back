# Generated by Django 4.2.7 on 2024-03-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyst2024app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('videos', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='question',
            field=models.CharField(default='Default', max_length=500),
        ),
        migrations.AddField(
            model_name='video',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
