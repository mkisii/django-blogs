from django.shortcuts import render
from .models import Post



# Create your views here.
def home(request):
	content = {

		'posts': Post.objects.all
	}
	return render(request, 'newblog/home.html', content)

def about(request):
	return render(request, 'newblog/about.html', { 'title': 'about'})
