# Generated by Django 2.0.5 on 2018-06-05 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_appli_student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='项目申请人'),
        ),
    ]
