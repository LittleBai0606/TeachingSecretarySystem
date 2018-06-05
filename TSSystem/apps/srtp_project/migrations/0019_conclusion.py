# Generated by Django 2.0.5 on 2018-06-05 18:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0018_auto_20180605_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion_file_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件名称')),
                ('conclusion_file_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件路径')),
                ('conclusion_deadline_date', models.DateField(default=django.utils.timezone.now, verbose_name='提交截止日期')),
                ('conclusion_check_status', models.CharField(choices=[('0', '未提交'), ('1', '审批中'), ('2', '已通过')], default='0', max_length=1, verbose_name='审核状态')),
                ('conclusion_check_point', models.CharField(choices=[('0', ''), ('1', '教师审核'), ('2', '教务处审核')], default='0', max_length=1, verbose_name='审核节点')),
                ('project_belong', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='srtp_project.Project', verbose_name='所属srtp项目')),
            ],
            options={
                'verbose_name': 'SRTP项目结题检查',
                'verbose_name_plural': 'SRTP项目结题检查',
            },
        ),
    ]
