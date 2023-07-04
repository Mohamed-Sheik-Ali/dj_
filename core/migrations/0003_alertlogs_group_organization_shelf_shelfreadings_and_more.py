# Generated by Django 4.2.2 on 2023-07-04 09:10

import core.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_username_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('sms_recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('readings', models.JSONField()),
                ('msg', models.CharField(blank=True, max_length=322, null=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_weight', models.FloatField()),
                ('total_units', models.IntegerField()),
                ('send_alert', models.BooleanField(default=False)),
                ('mail_alert', models.BooleanField(default=False)),
                ('sms_alert', models.BooleanField(default=False)),
                ('low_stock_threshold', models.IntegerField()),
                ('high_stock_threshold', models.IntegerField()),
                ('last_update_time', models.DateTimeField()),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.group')),
                ('organization_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ShelfReadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readings', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('shelf_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.shelf')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='country_code',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='group',
            name='organization_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization'),
        ),
        migrations.AddField(
            model_name='alertlogs',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization'),
        ),
        migrations.AddField(
            model_name='alertlogs',
            name='shelf_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.shelf'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
    ]
