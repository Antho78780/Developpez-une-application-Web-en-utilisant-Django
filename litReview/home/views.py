from django.shortcuts import render
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

class HomeView:
    @login_required(login_url="login")
    def home_page(request):
        return render(request, "home.html")

class TicketView:
    @login_required(login_url="login")
    def create_ticket(request):
        form = TicketForm()
        if request.method == "POST":
           pass
        return render(request, "ticket.html", context={"form": form})
    
# def create_review(request):
#     return render(request, "review.html")





