# Generated by Django 3.2.16 on 2023-04-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_allow_newsletters'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=256, verbose_name='role'),
        ),
    ]