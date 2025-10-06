from django.shortcuts import render, redirect

def root(request):
    if 'session' not in request.session:
        
        request.session['session'] = 1   
             
        context = {
            "x" : request.session['session']
        }
        return render (request,'index.html',context)

    else:
        request.session['session'] +=1        
        context = {
            "x" : request.session['session']
        }
        return render (request,'index.html',context)
        
    
    
def destroy_session(request):
    if 'session' not in request.session:
        return redirect ('/')
    
    else:

        del request.session['session']
        return redirect ('/')


    

