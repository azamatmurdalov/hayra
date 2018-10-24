from django.shortcuts import render

from .models import Volunteer

def volunteers(request):
	volunteer_list = Volunteer.objects.order_by('-date')[:20]
	context = {'volunteer_list': volunteer_list}
	return render(request, 'volunteers/volunteers.html', context)