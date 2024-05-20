from django.urls import path

from 먼작귀 import views

app_name='먼작귀'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]