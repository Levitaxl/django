from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('api/users/getAll/', views.get_all, name='users'),
    path('api/users/create/', views.create, name='users'),
    path('api/users/getProjects/<int:pk>/', views.get_user_and_project_by_id, name='users'),
    path('api/users/getProjects2/<int:pk>/', views.get, name='users'),
    path('', include(router.urls)),
]