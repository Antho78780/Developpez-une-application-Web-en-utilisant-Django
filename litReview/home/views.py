from django.shortcuts import render

def create_ticket(request):
    return render(request, "ticket_page.html")

def create_review(request):
    return render(request, "review_page.html")

def home_page(request):
    return render(request, "home_page.html")

def subscription_page(request):
    return render(request, "subscription_page.html")
