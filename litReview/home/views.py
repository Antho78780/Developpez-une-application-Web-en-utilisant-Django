from django.shortcuts import render
from .forms import TicketForm
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
    if request.method == "POST":
        print("Contenu envoyé")
    return render(request, "ticket.html", context={"form": TicketForm})
