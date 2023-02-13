from django.shortcuts import render
from .forms import register_forms

class register_user:
	def register(request):
		message = ""
		if request.method == "POST":
			form = register_forms(request.POST)
			if form.is_valid():
				form.save()
				message = "Enregistrement réussi"
			else:
				print("Informations incorrects")
				message = "N’utilisez pas de mots de passe faciles à deviner. N’utilisez pas d’information personnelle (comme votre date de naissance,votre ville natale ou le nom de votre animal)."

		return render(request, "register.html", context={"form": register_forms, "message": message})


# class Login_users:
# 	def login(request):
# 		message = ""
# 		if request.method == "POST":
# 			form = Login_forms(request.POST)
# 			if form.is_valid():
# 				user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
# 				if user is not None:
# 					login(request, user)
# 					message = f'Bienvenue, {user.username}! Vous êtes connecté.'
					
# 				else:
# 					print("compte non trouvé")
# 					message = "Identifiants invalides"
# 		return render(request, "login_page.html", context={"form": Login_forms, "message": message})

		
			



	


