# Generated by Django 5.0.4 on 2024-05-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qlnv", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nhanvien",
            name="loai_nhan_vien",
            field=models.CharField(max_length=10),
        ),
    ]
