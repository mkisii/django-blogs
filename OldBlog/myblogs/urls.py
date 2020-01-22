from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='myblogs-home'),
	path('about/', views.about, name='myblogs-about'),
]