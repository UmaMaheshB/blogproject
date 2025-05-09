from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
	# posts = Post.objects.all()
	posts = Post.objects.all().order_by("-id")
	return render(request, "home.html", {"posts": posts})

def news(request):
	return HttpResponse("this is news related posts")

def user_login(request):
	if request.method == "POST":
		# {"username": input_username, "password": "input_password"}
		print("request.POST: ", request.POST)
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			print(user)
			login(request, user) # main user login logic
			return redirect('blog-home')
	else:
		form = AuthenticationForm()
		return render(request, "login.html", {"form": form})

def user_logout(request):
	pass