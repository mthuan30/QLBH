# Generated by Django 4.2 on 2023-05-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Thongtin',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='namestore',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
