# Generated by Django 2.0.5 on 2018-06-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0030_auto_20180614_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$fNunPLrnHXQg$LB0XHtzPXTSed6cWqhaypNLacbJOZwr7nFstiUklYr4=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]