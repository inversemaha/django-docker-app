from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello(request):
    return HttpResponse("Hello, World!")

class GreetingView(View):
    def get(self, request):
        return HttpResponse("Greetings from the GreetingView!")