# Generated by Django 2.0.5 on 2018-06-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0033_auto_20180614_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$xrWLqczQYPQQ$KFijsn+hTnLwiMqU6erzMbCNGwZLF08f02ZygZc/FE8=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
