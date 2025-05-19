from django.shortcuts import redirect

def home(request):
	return redirect('blog-home')