from django.shortcuts import render,redirect

# Create your views here.
def root(request):
    return render(request,'index.html')
def result(request):
    request.session['first_name']=request.POST['first_name']
    request.session['Dojo_Location']=request.POST['Dojo_Location']
    request.session['favorite_language']=request.POST['favorite_language']
    request.session['comment']=request.POST['comment']
    return redirect('/display')

def display(request):
    return render(request,'result.html')
