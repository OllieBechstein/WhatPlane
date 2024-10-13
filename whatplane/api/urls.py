from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('planes/', views.getPlanes),
    path('planes/capture/', views.createPlane),
    path('planes/<str:pk>/delete/', views.deletePlane),
    path('planes/<str:pk>/', views.getPlane)
]
