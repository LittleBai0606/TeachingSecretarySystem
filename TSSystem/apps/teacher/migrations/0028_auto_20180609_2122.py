# Generated by Django 2.0.5 on 2018-06-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0027_auto_20180609_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$pTtijjBqfF9x$UnGzBVN3foS89A7NVsIK9FTMnXv7uAhk3nItIopbwuY=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]