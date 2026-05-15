from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    context = {
        "home" : "Hello World!"
    }
    
    return render(request, "home.html", context)

def create_ticket(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        Ticket.objects.create(
            title=title,
            description=description,
        )
        return redirect('create_ticket')
    return render(request, 'create_ticket.html')