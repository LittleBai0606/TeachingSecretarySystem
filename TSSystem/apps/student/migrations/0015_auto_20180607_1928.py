# Generated by Django 2.0.5 on 2018-06-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20180607_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='pbkdf2_sha256$100000$NmO2z6rnnx65$qN0q/et29d98yNQkg7ZUELw66mJ30ri2Q/pI/f7azEU=', max_length=100, verbose_name='学生账号密码'),
        ),
    ]
