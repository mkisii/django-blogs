from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='newblog-home'),
	path('about/', views.about, name='newblog-about')

]