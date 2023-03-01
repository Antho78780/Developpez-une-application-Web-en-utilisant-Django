from django.shortcuts import render
from .forms import RegisterForms
from django.shortcuts import redirect

def register_user(request):
	form = RegisterForms(request.POST if request.method == "POST" else None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect("account:login")
		else:
			print("Informations incorrects")

	return render(request, "register.html", locals())

			



	


