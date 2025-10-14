from django.shortcuts import render, redirect
from . import models
def index(request):
    context={
        'courses':models.Course.get_courses()
    }
    return render(request,'courses.html',context)

def add_course(request):
    models.Course.create_course(request.POST)
    return redirect('/')

def confirm_delete(request,courseid):
    context={
        "info":models.Course.get_course_info(courseid)
    }
    return render(request,'confirm_delete.html',context)


def delete_course(request,courseid):
    models.Course.delete_course(courseid)
    return redirect('/')