from django.contrib import admin

# Register your models here.
# 这里主要操作涉及到的是superuser操作界面
from .models import Grades, Students

from .models import Text
admin.site.register(Text)

class StudentsInfo(admin.TabularInline):
	model = Students
	extra = 2

class GradesAdmin(admin.ModelAdmin):
	inlines = [StudentsInfo]
	list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
	list_filter = ['gname']
	search_fields =['gname']
	list_per_page = 5

	#fields = ['ggirlnum','gboynum','gname','isDelete','gdate']
	fieldsets = [
		("num",{"fields":['ggirlnum','gboynum']}),
		("base",{"fields":['gname','gdate','isDelete']}),
	]
#将数据类型继续分类
#Register
admin.site.register(Grades, GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
	def gender(self):
		if self.sgender:
			return 'female'
		else:
			return 'male' 
			#针对布尔值类型数据进行转化
	gender.short_description = '性别'
	#针对英文列表头信息进行修改
	list_display = ['pk','sname',gender,'sage','scontent','isDelete','sgrade']
	#需要展示的信息有哪些
	list_per_page = 10
	actions_on_top = False
	actions_on_bottom = True
#admin.site.register(Students, StudentsAdmin)