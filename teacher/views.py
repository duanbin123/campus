# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from database.models import *
# Create your views here.
# def login(request):
#     return render(request,'login.html')

def base(request):
    return render(request,'base.html')

def t_course(request):
    if request.method=="GET":
        cou = Course.objects.all()
        return render(request, 'course.html',{'cou':cou})
    else:
        te_id = request.POST.get('t_code','')
        t_id = Teacher.objects.get(te_id=te_id)
        t_course=request.POST.get('t_course','')
        t_date=request.POST.get('t_date','')
        TeacherCourse.objects.create(rkDATE=t_date,teacher=t_id,course=Course.objects.get(cou_id=t_course))
        return HttpResponse('关联任课表成功')
        # return render(request,'course.html',{'cou':cou})

#创建班主任外键
def t_master(request):
    if request.method=='GET':
        cl = Clazz.objects.all()
        return render(request,'master.html',{'cl':cl})
    else:
            master_code = request.POST.get('master_code', '')
            clazz = request.POST.get('clazz','')
            start_date = request.POST.get('start_date','')
            print master_code,clazz,start_date
            HeadTeacher.objects.create(rkDATE=start_date,clazz = Clazz.objects.get(cla_id=clazz),teacher=Teacher.objects.get(te_id=master_code))
            return HttpResponse('关联班主任表成功')
#展示任课教师信息
def select_teacher(request):
    if request.method=='GET':
        id = request.GET.get('id')
        # print id
        TeacherCourse.objects.filter(id=id).delete()
        return render(request,'select_teacher.html')
    else:
        chaxun = request.POST.get('chaxun','')
        course = request.POST.get('course','')

        if chaxun=='任职科目':
            t_course = TeacherCourse.objects.filter(course=course)
            return render(request, 'select_teacher.html', {'t_course':t_course})
        if chaxun=='教师姓名':
            teacher = int(course)
            print teacher
            t1=[]
            t = TeacherCourse.objects.get(teacher=Teacher.objects.get(te_id=teacher))
            t1.append(t)
            return render(request, 'select_teacher2.html',{'t1':t1})

#展示班主任班级
def select_master(request):
    if request.method=='GET':
        id = request.GET.get('id','')
        if id:
            HeadTeacher.objects.filter(id = id).delete()
        return render(request,'select_master.html')
    else:
        chaxun = request.POST.get('chaxun')
        clazz = request.POST.get('clazz','')
        if chaxun =='班级':
            m_clazz = HeadTeacher.objects.filter(clazz=Clazz.objects.get(cla_id=clazz))
            return render(request,'select_master.html',{'m_clazz':m_clazz})
        if chaxun == '年级':
            grade = int(clazz)
            # print grade
            # print type(grade)
            grade = int(grade)
            # print grade
            clazz = Grade.objects.get(gr_id=grade).clazz_set.all()
            t = []
            for cls in clazz:
                # print cls
                cls1 = HeadTeacher.objects.get(clazz=cls)
                # print cls1.teacher.te_name
                cls2 = Teacher.objects.get(te_name=cls1.teacher.te_name)
                # print cls2
                t.append(cls2)
            return render(request, 'select_master2.html', {'t': t})
#查询任课教师信息
def show(request):
    if request.method=='GET':
        return render(request,'course1.html')
    else:
        t_code = request.POST.get('t_code')
        teachercourse = TeacherCourse.objects.filter(teacher=t_code)
        t_all = Teacher.objects.get(te_id=t_code).teachercourse_set.all()
        return render(request,'course1.html',{'teachercourse':teachercourse,'t_all':t_all})
#展示任职教师任职科目
# def show1(request):
#     if request.method=='GET':
#         return render(request,'select_teacher2.html')
#     else:


#展示班主任信息
def show2(request):
    if request.method=="GET":
        return render(request,'master1.html')
    else:
        master_code = request.POST.get('master_code','')
        # print master_code
        headteacher = HeadTeacher.objects.filter(clazz=Clazz.objects.get(cla_id=master_code))
        clazz_id = request.POST.get('clazz','')
        # print clazz_id
        clazz1 = Clazz.objects.all()
        head1 = HeadTeacher.objects.filter(teacher=master_code)
        return render(request,'master1.html',{'headteacher':headteacher,'clazz1':clazz1,'head1':head1})

