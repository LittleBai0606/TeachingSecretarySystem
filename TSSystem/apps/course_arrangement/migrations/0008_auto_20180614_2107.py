# Generated by Django 2.0.5 on 2018-06-14 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_arrangement', '0007_course_course_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_selection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_arrangement.Selection', verbose_name='资源分配'),
        ),
    ]
