# Generated by Django 2.0.5 on 2018-05-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180529_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$AjvgtUxdEOG0$KYj6tEnmk4VvJKto4Y/oAnbMJqUb3QArz8LLCPCjYhA=', max_length=100, verbose_name='学生账号密码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='pbkdf2_sha256$100000$vlftWCSwDPRI$YOWGE4MXXMcUmL7Yk3nUX8HigasCYL92eOdqC+km6CM=', max_length=100, verbose_name='教师账号密码'),
        ),
    ]
