# Generated by Django 4.2 on 2023-04-28 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_goimon_giatien_remove_goimon_mamon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goimon',
            name='thanhtien',
        ),
    ]
