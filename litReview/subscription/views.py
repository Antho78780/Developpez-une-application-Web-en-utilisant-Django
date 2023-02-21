from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def subscription(request):
    if request.method == "POST":
        print("recherhce du nom d'utilisateur")
    return render(request, "subscription.html")
