from django.db import models

# Create your models here.
#创建模板，实际就是创建数据库里所需要的表格类型
class Grades(models.Model):
	gname = models.CharField(max_length = 20)
	gdate = models.DateTimeField()
	ggirlnum = models.IntegerField()
	gboynum = models.IntegerField()
	isDelete = models.BooleanField(default = False)
	def __str__(self):
		return "%s-%d-%d"%(self.gname, self.ggirlnum, self.gboynum)
		#return self.gname
		
class StudentsManager(models.Manager):
	def get_queryset(self):
		return super(StudentsManager,self).get_queryset().filter(isDelete=False)
	def creatStudent(self, name, gender, age, content,isD, grade):
		stu = self.model()
		stu.sname = name
		stu.sage = age
		stu.sgender = gender
		stu.scontent = content
		stu.sgrade = grade
		return stu
		
class Students(models.Model):
	#stuObj = models.Manager() 
	#自定义管理器,如果上下两个管理器都存在，将以第一个方法实现，即未过滤
	stuObj1 = StudentsManager()
	#自定义模型管理器
	sname = models.CharField(max_length = 20)
	sgender = models.BooleanField(default = True)
	sage = models.IntegerField()
	scontent = models.CharField(max_length = 20)
	isDelete = models.BooleanField(default = False)
	sgrade = models.ForeignKey("Grades")
	def __str__(self):
		return self.sname
	
	class Meta:
		db_table = 'students'
		ordering = ['-id']
		
	@classmethod
	def creatStudent(cls, name, gender, age, content,isD, grade):
		stu = cls(sname=name, sage=age,sgender=gender,scontent=content,isDelete=isD,sgrade=grade)
		return stu

from tinymce.models import HTMLField
class Text(models.Model):
	str = HTMLField()