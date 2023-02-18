from django.shortcuts import render
from .forms import TicketForm, ReviewForm
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required(login_url="login")
def flux(request):
    ticket = Ticket.objects.all()
    return render(request, "flux.html", context={"ticket": ticket})


@login_required(login_url="login")
def create_ticket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect("home")
    return render(request, "ticket.html", context={"form": form})

@login_required(login_url="login")
def create_review(request):
    if request.method == "POST":
        print("Formulaire envoyé")

    return render(request, "review.html")





