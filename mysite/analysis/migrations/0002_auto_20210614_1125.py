# Generated by Django 3.2.3 on 2021-06-14 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'verbose_name': '家計簿', 'verbose_name_plural': '家計簿'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'カテゴリ'},
        ),
        migrations.AlterModelTable(
            name='analysis',
            table='kakeibo',
        ),
    ]
