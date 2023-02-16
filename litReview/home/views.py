from django.shortcuts import render
from .forms import TicketForm
from .models import Ticket
from django.contrib.auth.decorators import login_required

# def create_review(request):
#     return render(request, "review.html")

# def subscription_page(request):
#     return render(request, "subscription.html")

@login_required(login_url="login")
def home_page(request):
    return render(request, "home.html")

@login_required(login_url="login")
def create_ticket(request):
    form = TicketForm()
    if request.method == "POST":
        user = Ticket(title=request.POST["title"], description=request.POST["description"], image=request.POST["image"],user=request.user)
        user.save()
        print("Nom du compte :", request.user)
        
    return render(request, "ticket.html", context={"form": form})


