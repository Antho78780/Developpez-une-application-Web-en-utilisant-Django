from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, ReviewForm, FollowingForm, UnsubscribeForm
from .models import Ticket, Review, UserFollows
from django.contrib.auth.decorators import login_required
from account.models import User
from django.db import IntegrityError
from django.db.models import Q



@login_required
def flux(request):
    ticket = Ticket.objects.filter(Q(user=request.user) | Q(user__in=request.user.followed.all()))

    return render(request, "flux.html", context={"ticket": ticket})


@login_required
def create_ticket(request, ticket_id=None):
    if ticket_id is not None:
        ticket = get_object_or_404(Ticket, pk=ticket_id, user=request.user)
    
    form = TicketForm(request.POST if request.method == "POST" else None, request.FILES if request.method == "POST" else None, instance=ticket if ticket_id is not None else None)
    if request.method == "POST":
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect("flux:flux")

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
            return redirect("flux:flux")

    return render(request, "review.html", context={"formReview": formReview, "formTicket": formTicket})

@login_required
def create_review_response(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    review = ReviewForm()
    if request.method == "POST":
        review = ReviewForm(request.POST)
        if review.is_valid():
            review = review.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("flux:flux")


    return render(request, "review_response.html", context={"formReview": review, "ticket": ticket})

def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ReviewForm(request.POST if request.method == "POST" else None, instance=review)
    if request.method == "POST":
        if form.is_valid():
            form = form.save()
            return redirect("flux:posts")

    return render(request, "review.html", context={"formReview": form})

@login_required
def deleteTicket(request, ticket_id):
    get_object_or_404(Ticket, pk=ticket_id, user=request.user).delete()
    return redirect("flux:posts")

@login_required
def deleteReview(request, review_id):
    get_object_or_404(Review, pk=review_id, user=request.user).delete()
    return redirect("flux:posts")

@login_required
def subscription(request):
    userFollow =  UserFollows.objects.filter(Q(followed_user=request.user) | Q(user=request.user))
    form = FollowingForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        try:
            UserFollows.objects.create(followed_user=User.objects.get(username=form.cleaned_data["username"]), user=request.user)
            form = FollowingForm()
        except IntegrityError:
            form.add_error("username", "Vous suivez deja cette personne")

    return render(request, "subscription.html", context={"form": form, "userFollow": userFollow})

@login_required
def posts(request):
    review = Review.objects.all()
    ticket = Ticket.objects.all()
    return render(request, "posts.html", context={"review": review, "ticket": ticket})


@login_required
def deleteSubscription(request):
    form = UnsubscribeForm(request.POST)
    if form.is_valid():
        user_id = form.cleaned_data["user_id"]
        try:
            subscription = UserFollows.objects.get(pk=user_id)
            subscription.delete()
        except UserFollows.DoesNotExist:
            pass
    return redirect("flux:subscription")


    

    
        







