# Generated by Django 4.2 on 2023-04-27 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='goimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mamon', models.CharField(max_length=50, null=True)),
                ('tenmon', models.CharField(max_length=50, null=True)),
                ('giatien', models.FloatField()),
                ('thanhtien', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='loaimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenloai', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='thucdon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anh', models.CharField(max_length=50, null=True)),
                ('tenmon', models.CharField(max_length=50, null=True)),
                ('nguyenlieu', models.CharField(max_length=50, null=True)),
                ('maloai', models.CharField(max_length=50, null=True)),
                ('giatien', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('sdt', models.CharField(max_length=50, null=True)),
                ('hoten', models.CharField(max_length=50, null=True)),
                ('diachi', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
