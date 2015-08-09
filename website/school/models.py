from django.db import models
#coding:utf-8
# Create your models here.
class School(models.Model):
	school_id=models.AutoField(primary_key=True)
	school_name=models.CharField(max_length=30)
	
	

class Process(models.Model):
	school_id=models.ForeignKey(School)
	school_process_id=models.AutoField(primary_key=True)
	school_process=models.CharField(max_length=20)
	
	

class Student(models.Model):
	school_process_id=models.ForeignKey(Process)
	student_id=models.AutoField(primary_key=True)
	student_name=models.CharField(max_length=20)
	
	
