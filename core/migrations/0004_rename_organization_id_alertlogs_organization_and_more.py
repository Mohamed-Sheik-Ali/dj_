# Generated by Django 4.2.2 on 2023-07-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alertlogs_group_organization_shelf_shelfreadings_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alertlogs',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='alertlogs',
            old_name='shelf_id',
            new_name='shelf',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='shelf',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='shelf',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='shelfreadings',
            old_name='shelf_id',
            new_name='shelf',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='organization_id',
            new_name='organization',
        ),
    ]