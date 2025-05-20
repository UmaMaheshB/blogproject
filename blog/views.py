from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import example_data
from django.views import View
from django.contrib import messages
from . import forms

# Create your views here.
def home(request):
	# posts = Post.objects.all()
	posts = Post.objects.all().order_by("-id")
	return render(request, "home.html", {"posts": posts})

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'post_detail.html', {"post": post})

def post_delete(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if post.author != request.user:
		messages.warning(request, "you don't have rights to delete this post")
		return redirect("blog-home")

	if request.method == 'POST':
		post.delete()
		messages.info(request, f"{post.title} - Post deleted.")
		return redirect("blog-home")
	return render(request, "post_cofirm_delete.html", {'post': post})


def news(request):
	return HttpResponse('hello')

def category_posts(request, category_name):
	posts = Post.objects.filter(category__name=category_name).order_by("-id")
	return render(request, "home.html", {"posts": posts})

def user_login(request):
	if request.method == "POST":
		# {"username": input_username, "password": "input_password"}
		print("request.POST: ", request.POST)
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user) # main user login logic
			messages.info(request, "Logged-in successfully")
			return redirect('blog-home')
	else:
		form = AuthenticationForm()
	return render(request, "login.html", {"form": form})

def user_logout(request):
	logout(request)
	messages.info(request, "Loggedout successfully")
	return redirect('user-login')

# @login_required
# def new_category(request):
# 	if request.method == "GET":
# 		return render(request, 'new_category.html')
# 	if request.method == "POST":
# 		category_name = request.POST.get("category_name")
# 		Category.objects.create(name=category_name)
# 		return redirect('blog-home')

#class-based view
class NewCategory(View):
	def get(self, request):
		return render(request, 'new_category.html')

	def post(self, request):
		category_name = request.POST.get("category_name")
		Category.objects.create(name=category_name)
		messages.success(request, "New category added successfully :)")
		return redirect('blog-home')

def new_post(request):
	if request.method == "GET":
		form = forms.PostForm()
		return render(request, "post_form.html", {"form": form})
	if request.method == "POST":
		form = forms.PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			messages.success(request, "Post created successfully")
			return redirect("blog-home")
