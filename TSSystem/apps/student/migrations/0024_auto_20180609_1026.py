# Generated by Django 2.0.5 on 2018-06-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20180609_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$QdQXSwzRRXHQ$lglHHhaSeJ5sfib5QceESZfL1Ec8G63bsmIkMSNVLdk=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
