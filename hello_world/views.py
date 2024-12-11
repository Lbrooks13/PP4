from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'message': 'Hello, this is a message from the view!'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, World!")