# Generated by Django 4.2 on 2023-04-30 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_nguoidung_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nguoidung',
            name='session',
        ),
    ]