# Generated by Django 2.0.5 on 2018-06-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0018_auto_20180607_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$fxizf04j7Amf$pa2DYhHPu15ZOYYdSIoNMx4fR0JGUq7jaOW+gQOr/ck=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
