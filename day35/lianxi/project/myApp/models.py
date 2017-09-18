from django.db import models

# Create your models here.
# 一个模型类都在数据库中对应一张数据表
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gcount = models.IntegerField()
    gboynum = models.IntegerField()
    ggirlnum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    # 定义模型
    class Meta:
        # 元选项
        db_table = 'grades'
        ordering = ["-id"]

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)
    def createstudent(self,  name, sex, age, contend, grade, isDelete=False):
        stu = self.model()
        print(stu)
        stu.sname = name
        stu.ssex = sex
        stu.sage = age
        stu.scontend = contend
        stu.sgrade = grade
        return stu

class Students(models.Model):
    # 自定义模型管理器
    # 当自定义模型管理器，objects就不存在了
    stuObj = models.Manager()
    stuObj1 = StudentsManager()

    sname = models.CharField(max_length=20)
    ssex = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    sgrade = models.ForeignKey('Grades')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.sname
    class Meta:
        db_table = 'students'
        ordering = ["id"]

    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, sex, age, contend, grade, isDelete=False):
        stu = cls(sname = name, ssex = sex, sage = age, scontend = contend,
                  sgrade = grade)
        return stu
