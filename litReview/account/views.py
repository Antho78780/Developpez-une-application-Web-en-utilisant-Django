from django.shortcuts import render
from .models import User
from .forms import Login_forms, register_forms
from django.contrib.auth import authenticate

class Login_users:	
	def login(request):
		if request.method == "POST":
			form = Login_forms(request.POST)
			if form.is_valid():
				user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
				if user is not None:
					print("Compte trouvé: ", user)
				else:
					print("compte non trouvé")
			
		
	def print_login_html(request):
		return render(request, "login.html", context={"form": Login_forms,  "login": Login_users.login(request)})


class Register_users:
	def register(request):
		if request.method == "POST":
			form = register_forms(request.POST)
			if form.is_valid():
				user = form.save()

	def print_register_html(request):
		return render(request, "register.html", {"form": register_forms})



	


