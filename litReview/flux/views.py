from django.shortcuts import render
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def flux(request):
    ticket = Ticket.objects.all()
    review = Review.objects.all()
    return render(request, "flux.html", context={"ticket": ticket, "review": review})


@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect("flux")
    return render(request, "ticket.html", context={"form": form})

@login_required
def create_review_and_ticket(request):
    formReview = ReviewForm()
    formTicket = TicketForm()
    if request.method == "POST":
        formReview = ReviewForm(request.POST)
        formTicket = TicketForm(request.POST, request.FILES)

        if all([formReview.is_valid(), formTicket.is_valid()]):
            formTicket_save = formTicket.save(commit=False)
            formTicket_save.user = request.user
            formTicket_save.save()
            formReview_save = formReview.save(commit=False)
            formReview_save.user = request.user
            formReview_save.ticket = formTicket_save
            formReview_save.save()
            return redirect("flux")

    return render(request, "review.html", context={"formReview": formReview, "formTicket": formTicket})

@login_required
def create_review_response(request):
    formReview = ReviewForm()
    if request.method == "POST":
        formReview = ReviewForm(request.POST)

    return render(request, "review_response.html", context={"formReview": formReview})


@login_required
def posts(request):
    review = Review.objects.all()
    ticket = Ticket.Review.objects.all()
    return render(request, "posts.html", context={"review": review, "ticket": ticket})

@login_required
def subscription(request):
    if request.method == "POST":
        print("recherhce du nom d'utilisateur")
    return render(request, "subscription.html")






