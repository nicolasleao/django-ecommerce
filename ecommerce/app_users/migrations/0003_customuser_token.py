# Generated by Django 2.2.7 on 2019-11-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_users', '0002_remove_customuser_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(default='', max_length=64),
        ),
    ]
