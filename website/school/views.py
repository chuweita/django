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
	info=request.GET['info']
	school=request.GET['school']
	url='school?page=1'
	if info=="insert":
		sc=School.objects.filter(school_name=school)
		if len(sc)>0:
			return render(request,'info.html',{'info':'学校已存在','url':url})
		else:
			sc=School(school_name=school)
			sc.save()
			return render(request,'info.html',{'info':'学校添加成功','url':url})
	elif info=="select":
		sc=School.objects.filter(school_name=school)
		if len(sc)==0:
			return render(request,'info.html',{'info':'学校不存在','url':url})
		else:
			return render(request,'info.html',{'sc':sc,'url':url})
	else:
		school_new=request.GET['school_new']
		sc=School.objects.filter(school_name=school)
		if len(sc)==0:
			return render(request,'info.html',{'info':'学校不存在','url':url})
		else:
			sc[0].school_name=school_new
			sc[0].save()
			return render(request,'info.html',{'info':'修改成功','url':url})

def process(request):
	sc_id=request.GET['sc_id']
	pro=Process.objects.filter(school_id_id=sc_id)
	
	page=request.GET['page']
	page=int(page)*10
	a=[i+1 for i in range(len(pro)/11+1)]
	process=pro[page-10:page]
	return render(request,'process.html',{'process':process,'a':a,'sc_id':sc_id})
	
def add_process(request):
	info=request.GET['info']
	sc_id=request.GET['sc_id']
	process=request.GET['process']
	url="process?sc_id="+str(sc_id)+"&page=1"
	if info=="insert":
		pro=Process.objects.filter(school_process=process)
		if len(pro)>0:
				return render(request,'info.html',{'info':'专业已存在','url':url})
		else:
			proc=Process(school_process=process,school_id_id=sc_id)
			proc.save()
			return render(request,'info.html',{'info':'添加成功','url':url})
	elif info=="select":
		pro=Process.objects.filter(school_id_id=sc_id,school_process=process)
		if len(pro)==0:
			return render(request,'info.html',{'info':'专业不存在','url':url})
		else:
			return render(request,'info.html',{'pro':pro,'sc_id':sc_id,'url':url})
	else:
		process_new=request.GET['process_new']
		pro=Process.objects.filter(school_process=process)
		if len(pro)==0:
			return render(request,'info.html',{'info':'专业不存在','url':url})
		else:
			pro[0].school_process=process_new
			pro[0].save()
			return render(request,'info.html',{'info':'修改成功','url':url})

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
	info=request.GET['info']
	sc_id=request.GET['sc_id']
	pro_id=request.GET['pro_id']
	student=request.GET['student']
	url="student?sc_id="+sc_id+"&pro_id="+pro_id+"&page=1"
	
	if info=="insert":	
		stu=Student(school_process_id_id=pro_id,student_name=student)
		stu.save()
		return render(request,'info.html',{'info':'添加成功','url':url})
	elif info=="select":
		stu=Student.objects.filter(student_name=student,school_process_id_id=pro_id)
		if len(stu)==0:
			return render(request,'info.html',{'info':'不存在','url':url})
		else:
			return render(request,'info.html',{'stu':stu,'url':url}) 
	elif info=="delete":
		stu_id=request.GET['student_id']
		stu=Student.objects.filter(student_name=student,school_process_id_id=pro_id,student_id=stu_id)
		if len(stu)==0:
			return render(request,'info.html',{'info':'不存在','url':url})
		else:
			stu.delete()
			
			return render(request,'info.html',{'info':'删除成功','url':url})
	else:
		stu_id=request.GET['student_id']
		student_new=request.GET['student_new']
		stu=Student.objects.filter(student_name=student,school_process_id_id=pro_id,student_id=stu_id)
		if len(stu)==0:
			return render(request,'info.html',{'info':'不存在','url':url})
		else:
			stu[0].student_name=student_new
			stu[0].save()
			return render(request,'info.html',{'info':'修改成功','url':url})
