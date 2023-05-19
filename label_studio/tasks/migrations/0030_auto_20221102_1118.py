# Generated by Django 3.2.14 on 2022-11-02 11:18

from django.db import migrations
from tasks.functions import fill_annotations_project


def forward(apps, schema_editor):
    fill_annotations_project()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0029_annotation_project'),
    ]

    operations = [
        migrations.RunPython(forward, backwards),
    ]
