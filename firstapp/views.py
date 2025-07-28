from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationsForm

# Create your views here.
def hello(request):
    return HttpResponse("Hello, World!")

class GreetingView(View):
    def get(self, request):
        return HttpResponse("Greetings from the GreetingView!")

def home(request):
    form = ReservationsForm()

    if request.method == 'POST':
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation created successfully!")

    return render(request, 'index.html', {'form': form})