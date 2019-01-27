from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.manage, name='manage'),
    path('<int:id>/nourrir', views.nourrir, name='nourrir'),
    path('<int:id>/faire_exercice', views.faire_exercice, name='faire_exercice'),
    path('<int:id>/faire_dormir', views.faire_dormir, name='faire_dormir'),
    path('<int:id>/reveiller', views.reveiller, name='reveiller'),
]