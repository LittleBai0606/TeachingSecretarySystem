# Generated by Django 2.0.5 on 2018-06-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20180606_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$E3sIP1o8j33N$AY388IswuxUYYzRVhcipC+mZci8wuC8PO8dExXjRF9w=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
