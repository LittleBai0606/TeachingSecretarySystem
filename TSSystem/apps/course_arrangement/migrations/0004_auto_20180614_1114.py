# Generated by Django 2.0.5 on 2018-06-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_arrangement', '0003_auto_20180614_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_priority',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='selection',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='分配编号'),
        ),
    ]