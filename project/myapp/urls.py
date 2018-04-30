from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^(\d+)/$', views.detail),
	url(r'^grades/$', views.grades),
	url(r'^students/$', views.students),
	url(r'^grades/(\d+)$', views.gradesStudents),
	url(r'^addstudents/$', views.addstudents),
	url(r'^addstudents2/$', views.addstudents2),
	url(r'^stu/(\d+)$', views.studentspage),
	url(r'^studentssearch$', views.studentssearch),
	url(r'^studentsFQ$', views.practiceFQ),
	url(r'^attributes$', views.attributes),
	url(r'^get1', views.get1),
	url(r'^get2', views.get2),
	url(r'^showregister$', views.showregister),#表单注册页面
	url(r'^register/$', views.register),
	url(r'^cookietest$', views.cookietest),
	url(r'^redirect1$', views.redirect1),
	url(r'^redirect2$', views.redirect2),
	url(r'^main$', views.main),
	url(r'^login$', views.login),
	url(r'^showmain$', views.showmain),
	url(r'^quit$', views.quit),
	url(r'^good$', views.good,name='good'),
	url(r'^base$', views.base),
	url(r'^basebased$', views.basebased),
	url(r'^postinfo$', views.postinfo),
	url(r'^showinfo$', views.showinfo),
	url(r'^verifycode$', views.verifycode),
	url(r'^savefile$', views.savefile),
	url(r'^splitstudentpage/(\d+)$',views.splitstudentpage),
	url(r'^celery$',views.celery)
]