from django.shortcuts import render

class Login_users:	
	def print_login_html(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["pwd"]
			print(username, password)
		return render(request, 'login.html')


class Register_users:
	def print_register_html(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["pwd"]
			checked_pwd = request.POST["checked_pwd"]
			print(username, password, checked_pwd)
		
		return render(request, "register.html")



	


