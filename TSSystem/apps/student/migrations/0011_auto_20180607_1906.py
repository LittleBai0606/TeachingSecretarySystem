# Generated by Django 2.0.5 on 2018-06-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20180607_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$enB1mjMU37yp$IMIKTmW+PSTAoSwdTd8PCsdeLb2RU+3KCAY2JFMv+sw=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]