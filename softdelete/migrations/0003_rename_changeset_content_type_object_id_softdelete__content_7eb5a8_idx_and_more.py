# Generated by Django 4.2.4 on 2023-08-03 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdelete', '0002_auto_20170912_0537'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='changeset',
            new_name='softdelete__content_7eb5a8_idx',
            old_fields=('content_type', 'object_id'),
        ),
        migrations.RenameIndex(
            model_name='softdeleterecord',
            new_name='softdelete__content_faa170_idx',
            old_fields=('content_type', 'object_id'),
        ),
    ]
