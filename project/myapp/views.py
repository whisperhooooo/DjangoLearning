from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse('welcome')
def detail(request, num):
	return HttpResponse('detail-%s'%num)

	
from .models import Grades, Students

def grades(request):
	#去模板去数据
	gradesList = Grades.objects.all()
	#将数据传递给模板,模板再渲染页面，将渲染好的页面返回浏览器
	return render(request, 'myapp/grades.html',{'grades':gradesList})
def students(request):
	studentsList = Students.stuObj1.all()
	return render(request, 'myapp/students.html',{'students':studentsList,'str':'Alan is a good hoster','list1':['a','b'],'txt':False})
def gradesStudents(request,num):
	grade = Grades.objects.get(pk=num)
	studentsList = grade.students_set.all()
	return render(request, 'myapp/students.html',{'students':studentsList})
def addstudents(request):
	grade = Grades.objects.get(pk=3)
	stu = Students.creatStudent('Bob', 1, 10, 'Bob is joking', False, grade)
	stu.save()
	return HttpResponse('it works')
#可以将这个模型类方法和POST结合便可将用户注册的表单信息存到数据库中
def addstudents2(request):
	grade = Grades.objects.get(pk=1)
	stu = Students.stuObj1.creatStudent('Jay', 1, 12, 'Jay is singing', False, grade)
	stu.save()
	return HttpResponse('it works,too')
def studentspage(request,page):
	n = int(page)
	studentsList = Students.stuObj1.all()[(n-1)*5:n*5]
	return render(request, 'myapp/students.html',{'students':studentsList})
def studentssearch(request):
	#studentsList = Students.stuObj1.filter(sname__contains='k')
	#studentsList = Students.stuObj1.filter(sname__startswith='ke')
	#studentsList = Students.stuObj1.filter(pk__in=[2,4,6])
	#studentsList = Students.stuObj1.filter(sname__contains='%')
	#return render(request, 'myapp/students.html',{'students':studentsList})
	grade = Grades.objects.filter(students__scontent__contains='y')
	print(grade)
	return HttpResponse('okokokokokok!')
from django.db.models import F,Q
def practiceFQ(request):
	#g = Grades.objects.filter(ggirlnum__lt=F('gboynum'))
	g = Grades.objects.filter(ggirlnum__lt=F('gboynum')-56)
	print(g)
	return HttpResponse('ojbk')
def attributes(request):
	print(request.path)
	print(request.method)
	print(request.encoding)
	print(request.GET)
	print(request.POST)
	print(request.FILES)
	print(request.COOKIES)
	print(request.session)
	return HttpResponse('attributes')
def get1(request):
	a = request.GET.get('a')
	b = request.GET.get('b')
	c = request.GET.get('c')
	return HttpResponse(a+" "+b+" "+c)
def get2(request):
	a = request.GET.getlist('a')
	a1 = a[0]
	a2 = a[1]
	c = request.GET.get('c')
	return HttpResponse(a1+" "+a2+" "+c)
#POST
def showregister(request):
	return render(request, 'myapp/register.html')
def register(request):
	name = request.POST.get("name")
	gender = request.POST.get("gender")
	age = request.POST.get("age")
	hobby = request.POST.getlist("hobby")#由于这个是多选项
	print(name)
	print(gender)
	print(age)
	print(hobby)
	return HttpResponse('Successfully')
def cookietest(request):
	res = HttpResponse()
	cookie = request.COOKIES
	res.write("<h1>"+cookie["Alan"]+"</h1>")
	return res
	
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import logout

def redirect1(request):
	#return HttpResponseRedirect('/sunck/redirect2')
	return redirect('/sunck/redirect2')
def redirect2(request):
	return HttpResponse('重定向后的页面')
#以下三个函数的功能：首先我们进入到main网址→urls文件→mian函数→mian.html，在html页面下点击登陆后经过类似跳转到了login.html页面
#在html页面下需要输入用户名进行注册，注册后的信息给了showmain这个页面，showmain通过session将相应的username存储起来，然后重定向
#到main页面，此时由于username有了信息，就变化了。
def main(request):
	username = request.session.get('name',"游客")
	return render(request, 'myapp/main.html',{'username':username})
def login(request):
	return render(request, 'myapp/login.html')
def showmain(request):
	username = request.POST.get('username')
	request.session['name'] = username
	request.session.set_expiry(10)
	return redirect('/sunck/main')
def quit(request):
	#清除session
	#logout(request)
	request.session.clear()
	#request.session.flush()
	return redirect('/sunck/main')
def good(request):
	return render(request, 'myapp/good.html')
def base(request):
	return render(request, 'myapp/base.html',{'code':'<h1>Hey,Jude</h1>'})
def basebased(request):
	return render(request, 'myapp/basebased.html')
def postinfo(request):
	f = request.session.get('flag')
	str = ''
	if f == False:
		str = 'Please rewrite'
		request.session.clear()
	return render(request, 'myapp/postinfo.html',{'flag':str})
def showinfo(request):
	name = request.POST.get('username')
	pwd = request.POST.get('password')
	code1 = request.POST.get('verifycode').upper()
	code2 = request.session['verify'].upper()
	if code1 == code2:
		return render(request, 'myapp/showinfo.html',{'username':name,'password':pwd})
	else:
		request.session['flag'] = False
		return redirect('/sunck/postinfo')
	# 
	# str = ""
	# if f ==False:
	# return render(request, 'myapp/showinfo.html')
#验证码
from django.http import HttpResponse
def verifycode(request):
	#引入绘图模块
	from PIL import Image, ImageDraw, ImageFont
	#引入随机函数模块
	import random
	#定义变量，用于画面的背景色、宽、高
	bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
	width = 100
	height = 25
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0, 100):
		xy = (random.randrange(0, width), random.randrange(0, height))
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
		draw.point(xy, fill=fill)
	#定义验证码的备选值
	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	#随机选取4个值作为验证码
	rand_str = ''
	for i in range(0, 4):
		rand_str += str1[random.randrange(0, len(str1))]
	#构造字体对象
	font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 23)
	#font=ImageFont.load_default().font
	#构造字体颜色
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	#绘制4个字
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	#释放画笔
	del draw
	#存入session，用于做进一步验证
	request.session['verify'] = rand_str
	#内存文件操作
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')
import os
from django.conf import settings
def savefile(request):
	if request.method =="POST":
		f = request.FILES["file"]
		filePath = os.path.join(settings.MEDIA_ROOT,f.name)#文件路径拼接
		with open(filePath,'wb') as fp:
			for info in f.chunks():
				fp.write(info)
		return HttpResponse('Succeed!')
	else:
		return HttpResponse("Fail!")
from django.core.paginator import Paginator
def splitstudentpage(request, pageid):
	allList = Students.stuObj1.all()
	paginator = Paginator(allList,2)
	page = paginator.page(pageid)
	return render (request, 'myapp/splitstudentpage.html',{"students":page})
import time
def celery(request):
	print('1')
	time.sleep(5)
	print('2')
	return render (request, 'myapp/celery.html')
	