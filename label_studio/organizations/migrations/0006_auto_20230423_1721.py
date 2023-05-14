# Generated by Django 3.2.16 on 2023-04-23 10:21

from django.db import migrations
import datetime


class Migration(migrations.Migration):
    def add_all_permissions(apps=None, schema_editor=None):
        from django.contrib.auth.management import create_permissions

        if apps is None:
            from django.apps import apps

        for app_config in apps.get_app_configs():
            app_config.models_module = True
            create_permissions(app_config, verbosity=0)
            app_config.models_module = None

    dependencies = [
        ('organizations', '0005_invitedpeople'),
    ]

    operations = [
        migrations.RunPython(add_all_permissions, 
                             reverse_code=migrations.RunPython.noop)
    ]