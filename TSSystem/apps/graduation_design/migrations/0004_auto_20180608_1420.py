# Generated by Django 2.0.5 on 2018-06-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduation_design', '0003_auto_20180608_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='midtermreport',
            options={'verbose_name': '中期报告', 'verbose_name_plural': '中期报告'},
        ),
        migrations.AlterField(
            model_name='midtermreport',
            name='student_belong',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='创作学生'),
        ),
        migrations.AlterField(
            model_name='openingreport',
            name='student_belong',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='创作学生'),
        ),
    ]
