#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from school.models import School
from school.models import Process
from school.models import Student

def index(request):
	return render(request,'index.html')

def school(request):
	
	page=request.GET['page']
	page=int(page)*10
	school=School.objects.all()
	lenth=len(school)/11+1
	a=[i+1 for i in range(lenth)]
	school=school[page-10:page]
	return render(request,'school.html',{'school':school,'a':a})
	
def add_school(request):
	school=request.GET['school']
	al=School.objects.all()
	for i in al:
		if school==i.school_name:
			return render(request,'info.html',{'info':'已存在','url':'school?page=1'})
	sc=School(school_name=school)
	sc.save()
	return render(request,'info.html',{'info':'添加成功','url':'school?page=1'})

def process(request):
	sc_id=request.GET['sc_id']
	pro=Process.objects.filter(school_id_id=sc_id)
	
	page=request.GET['page']
	page=int(page)*10
	a=[i+1 for i in range(len(pro)/11+1)]
	process=pro[page-10:page]
	return render(request,'process.html',{'process':process,'a':a,'sc_id':sc_id})
	
def add_process(request):
	sc_id=request.GET['sc_id']
	url="process?sc_id="+str(sc_id)+"&page=1"
	process=request.GET['process']
	pro=Process.objects.filter(school_id_id=sc_id)
	for i in pro:
		if process==i.school_process:
			return render(request,'info.html',{'info':'已存在','url':url})
	proc=Process(school_process=process,school_id_id=sc_id)
	proc.save()
	return render(request,'info.html',{'info':'添加成功','url':url})

def student(request):
	sc_id=request.GET['sc_id']
	pro_id=request.GET['pro_id']
	page=request.GET['page']
	stu=Student.objects.filter(school_process_id_id=pro_id)
	page=int(page)*10
	student=stu[page-10:page]
	a=[i+1 for i in range(len(stu)/11+1)]
	return render(request,'student.html',{'student':student,'a':a,'sc_id':sc_id,'pro_id':pro_id})

def add_student(request):
	sc_id=request.GET['sc_id']
	pro_id=request.GET['pro_id']
	student=request.GET['student']
	url="student?sc_id="+sc_id+"&pro_id="+pro_id+"&page=1"
	#stu=Process.objects.filter(school_process_id_id=pro_id)
	stu=Student(school_process_id_id=pro_id,student_name=student)
	stu.save()
	return render(request,'info.html',{'info':'添加成功','url':url})
