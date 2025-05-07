from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
	# posts = Post.objects.all()
	posts = Post.objects.all().order_by("-id")
	return render(request, "home.html", {"posts": posts})

def news(request):
	return HttpResponse("this is news related posts")