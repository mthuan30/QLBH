# Generated by Django 4.2 on 2023-04-28 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_goimon_ctgoimon_ctgoimon_goimon'),
    ]

    operations = [
        migrations.AddField(
            model_name='goimon',
            name='thoigiangoi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
