# Generated by Django 2.0.5 on 2018-06-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_auto_20180609_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$jszo9Xe0yCle$Yj5xRzJh1FovCItBlFJ4h8d16dcG9qnLxDqZtl/iRdI=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
