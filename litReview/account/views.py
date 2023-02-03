from django.shortcuts import render

class Login_users:	
	def login(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["pwd"]
			print(username, password)
			return {
				"username": username,
				"password": password
			}
	
	def print_login_html(request):
		object_login = Login_users.login(request)
		return render(request, "login.html", print(object_login))


class Register_users:
	def register(request):
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["pwd"]
			checked_pwd = request.POST["checked_pwd"]
			return {
				"username": username,
				"password": password, 
				"checked_password": checked_pwd
			}	

	def print_register_html(request):
		object_register = Register_users.register(request)
		return render(request, "register.html", print(object_register))



	


