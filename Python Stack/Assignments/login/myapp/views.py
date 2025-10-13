from django.shortcuts import render, redirect
from . import models

import bcrypt

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        errors = models.User.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            context = {'errors':errors}
            return render(request,'index.html',context)
        else:
            user = models.register(request.POST)
            request.session['login'] = True
            request.session['user_id'] = user.id 
            request.session['email'] = user.email
            return redirect("/success")
        
def open_home(request):
    if request.session['login'] == True:
        if 'user_id' in request.session:
            context = {'user':models.get_user(request.session['email'])}
            return render(request,"home.html",context)
    else: 
        return render(request, "not_logged_in.html")
    

def logout(request):
    request.session.clear()
    request.session['login'] = False
    return redirect('/')


def login(request):
    errors = {}
    if request.method == 'POST':
        if (models.is_exists(request.POST['email'])):
            user = models.get_user(request.POST['email'])
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                request.session['login'] = True
                request.session['email'] = user.email
                return redirect('/success')
            else: 
                errors['login_password'] = 'Incorrect password please try again'
                context = {'errors':errors}
                return render(request,'index.html',context)
        else:
            errors['login_email'] = 'Invalid Email address'
            context = {'errors':errors}
            return render(request,'index.html',context)       