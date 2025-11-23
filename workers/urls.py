from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('<int:pk>/', views.worker_detail, name='worker_detail'),
    path('my-profile/', views.my_profile, name='my_profile'),
]

