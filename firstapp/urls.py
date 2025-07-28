from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello),
    path('class', views.GreetingView.as_view()),
]