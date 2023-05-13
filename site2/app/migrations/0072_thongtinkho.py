# Generated by Django 4.2 on 2023-05-11 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_alter_nhanvien_giocong'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThongtinKho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluongnhap', models.IntegerField(null=True)),
                ('ngaynhap', models.DateTimeField(auto_now_add=True)),
                ('nvl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.khohang')),
            ],
        ),
    ]