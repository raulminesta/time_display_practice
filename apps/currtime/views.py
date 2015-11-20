from django.shortcuts import render
from time import strftime
current_date = strftime('%b %-d, %Y')
current_time = strftime('%I:%M %p')
def index(request):
	context = {
		'date': current_date,
		'time': current_time,
	}
	return render(request, 'currtime/index.html', context)
