from django.urls import path
from . import views

urlpatterns = [
	path('', views.volunteers, name='volunteers'),
	path('register/', views.register, name='register'),
	path('message/', views.message, name='message')
]