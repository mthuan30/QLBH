# Generated by Django 4.2 on 2023-05-04 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_remove_loaimon_maloai_remove_thucdon_maloai_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='thucdon',
            name='Loaimon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.loaimon'),
        ),
    ]
