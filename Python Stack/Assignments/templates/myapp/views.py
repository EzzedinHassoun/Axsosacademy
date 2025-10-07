from django.shortcuts import render,redirect
from .models import User


# Create your views here.
def index(request):
    users=User.getallusers()
    context = {
        'users':users
    }
    print(users)
    return render(request, 'index.html',context)

def user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        post_data={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'age':age
        }

        user=User.create_user(post_data)
        return redirect ( '/')
