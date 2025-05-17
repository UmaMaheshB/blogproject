from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import example_data
from django.views import View

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
		return HttpResponse("<p style='color:red'>you don't have rights to delete this post</p>")

	if request.method == 'POST':
		post.delete()
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
			return redirect('blog-home')
	else:
		form = AuthenticationForm()
	return render(request, "login.html", {"form": form})

def user_logout(request):
	logout(request)
	return redirect('user-login')

# def new_category(request):
# 	if request.method == "GET":
# 		return render(request, 'new_category.html')
# 	if request.method == "POST":
# 		category_name = request.POST.get("category_name")
# 		Category.objects.create(name=category_name)
# 		return redirect('blog-home')

class NewCategory(View):
	def get(self, request):
		return render(request, 'new_category.html')

	def post(self, request):
		category_name = request.POST.get("category_name")
		Category.objects.create(name=category_name)
		return redirect('blog-home')

