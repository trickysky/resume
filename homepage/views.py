from django.shortcuts import render


# Create your views here.

def index(request):
	return render(request, 'homepage/index.html', set_index())


def set_index():
	return {}
