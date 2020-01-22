from django.shortcuts import render

posts = [
	{

		'author': 'Obed',
		'title': 'Myblogs post1',
		'content': 'My first Post content',
		'date_posted': 'Oct 7 2019', 
	},

	{
	 	'author': 'Obed ',
		'title': 'Myblogs post 2',
		'content': 'My secPost content',
		'date_posted': 'Oct 7, 2019',
	}
]
 
# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'myblogs/home.html', context)


def about(request):
	 return render(request, 'myblogs/about.html', {'title': 'about'})
