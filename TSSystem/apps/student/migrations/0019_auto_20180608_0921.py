# Generated by Django 2.0.5 on 2018-06-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20180607_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$Yjapl1x3dUSe$cDB9mIdpGmycgUXWa9rb2ltRfFNF9ZExqVhVG61ngro=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
