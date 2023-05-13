# Generated by Django 4.2 on 2023-04-28 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_taikhoan_thongtin_thucdon_mamon_delete_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taikhoan',
            new_name='Nguoidung',
        ),
        migrations.CreateModel(
            name='Nhanvien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('sdt', models.CharField(max_length=50, null=True)),
                ('hoten', models.CharField(max_length=50, null=True)),
                ('diachi', models.CharField(max_length=50, null=True)),
                ('manguoidung', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.thongtin')),
            ],
        ),
    ]
