# Generated by Django 4.2.2 on 2023-07-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_is_supervisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_supervisor',
        ),
    ]