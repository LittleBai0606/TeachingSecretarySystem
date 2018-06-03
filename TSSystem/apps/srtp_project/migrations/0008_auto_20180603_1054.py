# Generated by Django 2.0.5 on 2018-06-03 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20180603_1054'),
        ('srtp_project', '0007_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_student',
        ),
        migrations.AddField(
            model_name='project',
            name='project_appli_student',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Student', verbose_name='项目申请人'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_member',
            field=models.CharField(blank=True, default='暂未填写', max_length=50, null=True, verbose_name='项目成员'),
        ),
    ]