# Generated by Django 2.0.5 on 2018-06-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0041_auto_20180616_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$SEDAbqlylaLl$8mSCMQLH2beXQ4hXvkaF4oV9MuTsK+7PvVDgI1FmQbY=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
