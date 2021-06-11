# Generated by Django 3.2.4 on 2021-06-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='arrive_time',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='時間'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('女性', '女性'), ('男性', '男性')], max_length=2, null=True, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.job'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='join_date',
            field=models.DateField(null=True, verbose_name='入会日'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=300, null=True, verbose_name='住所'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='名前'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=255, null=True, verbose_name='電話番号'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.purpose'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='stop_date',
            field=models.DateField(blank=True, null=True, verbose_name='退会日'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='trigger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.trigger'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='生年月日'),
        ),
    ]