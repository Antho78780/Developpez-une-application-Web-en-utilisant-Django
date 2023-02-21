from django.shortcuts import render
from .forms import register_forms, Login_forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def register_user(request):
	message = ""
	if request.method == "POST":
		form = register_forms(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
		else:
			print("Informations incorrects")
			message = "N’utilisez pas de mots de passe faciles à deviner. N’utilisez pas d’information personnelle (comme votre date de naissance,votre ville natale ou le nom de votre animal)."

	return render(request, "register.html", context={"form": register_forms, "message": message})


def login_user(request):
	message = ""
	if request.method == "POST":
		form = Login_forms(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
			if user is not None:
				login(request, user)
				return redirect("flux")
			else:
				message = "L'identifiant ou le mot de passe que vous avez saisi(e) n’est pas associé(e) à un compte. Trouvez votre compte et connectez-vous."
	if request.user.is_anonymous:
		return render(request, "login.html", context={"form": Login_forms, "message": message})
	else:
		return redirect("flux")

def logout_user(request):
	logout(request)
	return redirect("login")
	
			



	


