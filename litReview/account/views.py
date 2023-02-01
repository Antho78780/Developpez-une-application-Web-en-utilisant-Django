from django.shortcuts import render

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["pwd"]
		print(username, password)
	return render(request, 'login.html')

def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["pwd"]
		checked_pwd = request.POST["checked_pwd"]
		print(username, password, checked_pwd)
	return render(request, "register.html")

	


