# Generated by Django 2.0.5 on 2018-06-09 17:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edu_reform', '0003_eduproject_eduproject_select_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edufund_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='具体支出项目摘要')),
                ('edufund_type', models.CharField(choices=[('1', '差旅费'), ('2', '实验费'), ('3', '资料费'), ('4', '实验耗材费'), ('5', '计算机小型存储设备费'), ('6', '邮寄费'), ('7', '论文版面费'), ('8', '成果鉴定费'), ('9', '专利申请费'), ('10', '文件检索费'), ('11', '办公费'), ('12', '其他费用')], default='12', max_length=9, verbose_name='经费类别')),
                ('edufund_num', models.IntegerField(blank=True, null=True, verbose_name='经费支出金额')),
                ('edufund_date', models.DateField(default=django.utils.timezone.now, verbose_name='经费支出日期')),
                ('eduproject_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_reform.EduProject', verbose_name='所属教改/教研/教材项目')),
            ],
            options={
                'verbose_name_plural': '经费管理',
                'verbose_name': '经费管理',
            },
        ),
        migrations.CreateModel(
            name='EduResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eduresult_name', models.CharField(default='未命名成果', max_length=50, verbose_name='项目成果名称')),
                ('eduresult_type', models.CharField(choices=[('1', '著作/著作权'), ('2', '论文'), ('3', '专利'), ('4', '实物'), ('5', '软件/图纸/设计'), ('6', '获奖证书'), ('7', '其他')], default='7', max_length=8, verbose_name='项目成果类型')),
                ('eduresult_date', models.DateField(default=django.utils.timezone.now, verbose_name='项目成果日期')),
                ('eduresult_master', models.CharField(default='未填写', max_length=20, verbose_name='项目成果所有人')),
                ('eduresult_file_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='项目附件名称')),
                ('eduresult_file_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='项目附件路径')),
                ('eduproject_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_reform.EduProject', verbose_name='所属srtp项目')),
            ],
            options={
                'verbose_name_plural': '成果管理',
                'verbose_name': '成果管理',
            },
        ),
    ]
