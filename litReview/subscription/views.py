from django.shortcuts import render

def subscription(request):
    if request.method == "POST":
        pass
    return render(request, "subscription.html")
