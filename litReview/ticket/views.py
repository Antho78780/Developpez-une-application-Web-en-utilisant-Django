from django.shortcuts import render

def ticket(request):
    return render(request, "ticket.html")

def critique(request):
    return render(request, "critique.html")

def flux(request):
    return render(request, "flux.html")
