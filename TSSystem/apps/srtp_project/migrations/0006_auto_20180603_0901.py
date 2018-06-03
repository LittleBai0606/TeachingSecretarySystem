# Generated by Django 2.0.5 on 2018-06-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0005_auto_20180601_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_appli_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='项目申请书名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_appli_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='项目申请书路径'),
        ),
    ]
