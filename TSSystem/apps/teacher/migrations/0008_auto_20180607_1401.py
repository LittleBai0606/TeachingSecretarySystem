# Generated by Django 2.0.5 on 2018-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20180607_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$zpweVUNz4ycu$sF/IAtbI6IHK1UeQ+fzBGvpZt+wssmCbsxvi0a+fj5Q=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
