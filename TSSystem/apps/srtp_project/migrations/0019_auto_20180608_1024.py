# Generated by Django 2.0.5 on 2018-06-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srtp_project', '0018_auto_20180608_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notififile',
            name='notifi_belong',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='NotifiFile',
        ),
    ]
