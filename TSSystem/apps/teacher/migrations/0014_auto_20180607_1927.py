# Generated by Django 2.0.5 on 2018-06-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_auto_20180607_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$FNCFNlnxnvR6$DauSAwPzt+5UB9/eni/OGXyWt2A5UssD9oL2dedE7aE=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]