from django.db import models


#
# # Create your models here.
# class Stu(models.Model):
#     '''自定义Stu表对应的model类'''
#     #定义属性，默认主键自增id字段可不写
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=16)
#     age=models.SmallIntegerField()
#     sex=models.CharField
#     classid=models.CharField()
#
#     #定义默认输出格式
#     def __str__(self):
#         return "%d:%s:%d:%s:%s:"(self.id ,self.name ,self.age ,self.sex ,self.classid)
#
#     #自定义对应的表名，默认表名blog_stu
#     class Meta:
#         db_table="stu"
#
#
class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18, db_column='age')

    # False代表男   True代表女
    p_sex = models.BooleanField(default=32, null=True, blank=True)
    p_hobby = models.CharField(max_length=32, null=True, blank=True)

    @classmethod
    def create(cls, p_name, p_age=100, p_sex=True, p_hobby='gaming'):
        #实现参数自定义
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta():
        db_table = "People"
