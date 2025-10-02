from django.shortcuts import render
from time import gmtime, strftime 


def index(request):
    current_time = strftime("%B %d, %Y %I:%m %p", gmtime())
    
    context = {
        "time": current_time
    }
    return render(request, 'index.html', context)