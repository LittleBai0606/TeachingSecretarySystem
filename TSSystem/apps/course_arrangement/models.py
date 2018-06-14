from django.db import models
from teacher.models import Teacher
from main_platform.models import Class

# Create your models here.



class Selection(models.Model):

    COURSE_PERIOD_CHOICE = (
        (1, '1-8'),
        (2, '9-16'),
    )

    COURSE_WEEKDAY_CHOICE = (
        (1, '星期一'),
        (2, '星期二'),
        (3, '星期三'),
        (4, '星期四'),
        (5, '星期五')
    )

    COURSE_TIME_CHOICE = (
        (1, '第一节'),
        (2, '第二节'),
        (3, '第三节'),
        (4, '第四节'),
        (5, '第五节'),
        (6, '第六节')
    )


    COURSE_BUILDING_CHOICE = (
        (1, '逸夫楼'),
        (2, '教学楼'),
        (3, '机电楼'),
    )

    IS_EMPTY_CHOICE = (
        (True, '可以分配'),
        (False, '不可分配')
    )

    course_period = models.IntegerField(null=False, blank=False, choices=COURSE_PERIOD_CHOICE, default=1, verbose_name=u'课程周期')
    course_weekday = models.IntegerField(null=False, blank=False, choices=COURSE_WEEKDAY_CHOICE, default=1, verbose_name=u'课程上课日')
    course_time = models.IntegerField(null=False, blank=False, choices=COURSE_TIME_CHOICE, default=1, verbose_name=u'课程时间')
    course_building = models.IntegerField(null=False, blank=False, choices=COURSE_BUILDING_CHOICE, default=1, verbose_name=u'课程建筑')
    course_classroom = models.IntegerField(null=True, blank=True, default=999, verbose_name=u'上课教室')
    selection = models.IntegerField(null=True, blank=True, editable=False, default=0, verbose_name='分配编号')
    is_empty = models.BooleanField(choices=IS_EMPTY_CHOICE, default=True, verbose_name='分配情况')

    class Meta:
        verbose_name = u'课程资源分配'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%d]' %(self.selection)

    def save(self, *args, **kwargs):
        period = self.course_period * 1000000
        weekday = self.course_weekday * 100000
        time = self.course_time * 10000
        building = self.course_building * 1000
        selection = period + weekday + time + building + self.course_classroom
        self.selection = selection
        super(Selection, self).save(*args, **kwargs)







class Course(models.Model):

    #课程
    COURSE_POINT_CHOICE = (
        (64, 64),
        (32, 32),
        (16, 16)
    )

    COURSE_TYPE_CHOICE = (
        (5, '必修'),
        (0, '专选')
    )

    course_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'课程编号')
    course_name = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'课程名称')
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u'授课老师')
    course_point = models.IntegerField(null=False, blank=False, default=1, choices=COURSE_POINT_CHOICE, verbose_name=u'课程学时')
    course_type = models.IntegerField(null=False, blank=False, choices=COURSE_TYPE_CHOICE, default=0, verbose_name=u'课程类型')
    course_capacity = models.IntegerField(null=False, blank=False, default=0, verbose_name=u'课程容量')
    course_selection = models.ForeignKey(null=True, blank=True, Selection, on_delete=models.CASCADE, verbose_name=u'资源分配')
    course_priority = models.IntegerField(null=True, blank=True, editable=False, default=0, verbose_name='优先级')
    course_class = models.ManyToManyField(Class, default='上课班级')

    class Meta:
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[%s %d]' %(self.course_name, self.course_point)

    def save(self, *args, **kwargs):
        self.course_priority = self.course_point * self.course_type + self.course_point
        super(Course, self).save(*args, **kwargs)








