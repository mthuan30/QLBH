# Generated by Django 4.2 on 2023-04-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_nguoidung_thongtin_nguoidung_manguoidung_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nguoidung',
            name='phien',
            field=models.CharField(max_length=50, null=True),
        ),
    ]