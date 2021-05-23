from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('prosc',views.prosc),
    path('result',views.result),
    path('winner',views.winner),
    path('play_again', views.play_again)


]
