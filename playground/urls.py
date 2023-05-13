from django.urls import path
from . import views
#url configratn
urlpatterns =[
    path('hello', views.say_hello)
] 