# Generated by Django 4.2 on 2023-04-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_thucdon_anh'),
    ]

    operations = [
        migrations.AddField(
            model_name='loaimon',
            name='maloai',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
