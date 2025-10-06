from django.shortcuts import render , redirect
import random
def index(request):
    if "number" not in request.session:
        request.session["number"] = random.randint(1,100)
        request.session["attempts"] = 0
        request.session["message"] = ""
        request.session["color"] = "black"

    return render(request, "index.html")

def guess(request):
    if request.method == "POST":
        guess = int(request.POST.get("guess", 0))
        request.session["attempts"] += 1 
    
    if guess < request.session["number"]:
        request.session["message"] = "Too low!"
        request.session["color"] = "blue"  
    elif guess > request.session["number"]:
        request.session["message"] = "Too high!"
        request.session["color"] = "red"
    else:
        request.session["message"] = f"Correct! You got it in {request.session['attempts']} attempts."
        request.session["color"] = "green"
    
    return redirect("index")

def playAgain(request):
    request.session.flush()
    return redirect("index")

