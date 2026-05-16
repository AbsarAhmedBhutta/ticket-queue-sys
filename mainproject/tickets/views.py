from django.shortcuts import render, redirect
from .models import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def home(request):
    context = {
        "home" : "Hello World!"
    }
    
    return render(request, "home.html", context)

def create_ticket(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        ticket = Ticket.objects.create(
            title=title,
            description=description,
        )
        
        channel_layer = get_channel_layer()
        
        async_to_sync(channel_layer.group_send)(
            "tickets_dashboard",
            {
            "type":"ticket_created",
            "ticket": {
                "id": ticket.id,
                "title": ticket.title,
                "description": ticket.description,
                "status": ticket.status if ticket.status else "PENDING",
            }}
        )
        return redirect('create_ticket')
    
    return render(request, 'create_ticket.html')

def agent_dashboard(request):
    tickets = Ticket.objects.all().order_by("-created_at")

    return render(request, "dashboard.html", {
        "tickets": tickets
    })