# Generated by Django 2.0.5 on 2018-06-08 10:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifi_id', models.IntegerField(default=1528424654, unique=True, verbose_name='通知id')),
                ('notifi_date', models.DateField(default=django.utils.timezone.now, verbose_name='通知发布时间')),
                ('notifi_title', models.CharField(default='未命名消息通知', max_length=50, verbose_name='通知标题')),
                ('notifi_content', models.TextField(blank=True, null=True, verbose_name='通知内容')),
            ],
            options={
                'verbose_name': '消息通知',
                'verbose_name_plural': '消息通知',
            },
        ),
        migrations.CreateModel(
            name='NotifiFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifi_file_name', models.CharField(blank=True, default='暂未命名', max_length=100, null=True, verbose_name='通知附件名称')),
                ('notifi_file_url', models.FileField(blank=True, default='', null=True, unique=True, upload_to='SrtpNotification/', verbose_name='通知附件路径')),
                ('notifi_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_platform.Notification', verbose_name='所属通知')),
            ],
            options={
                'verbose_name': '通知附件',
                'verbose_name_plural': '通知附件',
            },
        ),
    ]
