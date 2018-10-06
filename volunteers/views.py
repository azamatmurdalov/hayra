from django.shortcuts import render

def volunteers(request):
	return render(request, 'volunteers/volunteers.html', locals())
