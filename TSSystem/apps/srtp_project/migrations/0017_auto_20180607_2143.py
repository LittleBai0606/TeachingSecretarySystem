# Generated by Django 2.0.5 on 2018-06-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0016_auto_20180607_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notifi_id',
            field=models.IntegerField(default=1528379023, unique=True, verbose_name='通知id'),
        ),
    ]
