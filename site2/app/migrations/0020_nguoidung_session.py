# Generated by Django 4.2 on 2023-04-30 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('app', '0019_remove_nguoidung_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='nguoidung',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
        ),
    ]
