from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('planes/', views.getPlanes),
    path('planes/capture/', views.capturePlane),
    path('planes/delete/', views.deletePlane),
    path('planes/<str:pk>/', views.getPlane),
    path('planes/top', views.getScores),
]
