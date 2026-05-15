from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "home" : "Hello World!"
    }
    
    return render(request, "home.html", context)