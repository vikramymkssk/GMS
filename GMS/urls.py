from django.urls import path
from .import views

urlpatterns = [
    path('', views.GMS_list, name='GMS_list'),
    path('GMS/<int:pk>/', views.GMS_detail, name='GMS_detail'),
]