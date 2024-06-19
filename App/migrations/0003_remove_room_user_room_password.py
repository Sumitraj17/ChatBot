# Generated by Django 5.0.6 on 2024-06-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_room_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(default='password', max_length=12),
            preserve_default=False,
        ),
    ]
