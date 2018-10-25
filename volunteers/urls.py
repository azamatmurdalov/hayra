from django.urls import path

from . import views

app_name = 'volunteers'
urlpatterns = [
	path('', views.volunteers, name='volunteers'),
	path('register/', views.register, name='register'),
	path('message/', views.message, name='message')
]