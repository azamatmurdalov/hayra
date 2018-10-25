from django.shortcuts import redirect, render
from .forms import PostForm

from .models import Volunteer

def volunteers(request):
	volunteer_list = Volunteer.objects.order_by('-date')[:20]
	context = {'volunteer_list': volunteer_list}
	return render(request, 'volunteers/volunteers.html', context)

def register(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect('message')
	else:
		form = PostForm()
	return render(request, 'volunteers/register.html', {'form': form})

def message(request):
	return render(request, 'volunteers/message.html')