# Generated by Django 4.1.12 on 2024-03-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_rnaseq"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rnaseq",
            name="filepath",
        ),
        migrations.AddField(
            model_name="rnaseq",
            name="file_path",
            field=models.CharField(default="", max_length=255, verbose_name="文件路径"),
        ),
    ]
