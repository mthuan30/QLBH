# Generated by Django 4.2 on 2023-04-29 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_khohang_rename_email_nhanvien_manhanvien_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goimon',
            name='giatien',
        ),
        migrations.AddField(
            model_name='goimon',
            name='manguoidung',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.thongtin'),
        ),
        migrations.AlterField(
            model_name='thucdon',
            name='maloai',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
