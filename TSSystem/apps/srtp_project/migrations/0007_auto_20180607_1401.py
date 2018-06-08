# Generated by Django 2.0.5 on 2018-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0006_auto_20180607_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_subject',
            field=models.CharField(blank=True, default='暂未填写', max_length=20, null=True, verbose_name='项目所属学科'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notifi_id',
            field=models.IntegerField(default=1528351261, unique=True, verbose_name='通知id'),
        ),
    ]