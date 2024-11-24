from django.urls import path, include
from rest_framework import routers
from .api import ProjectViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('api/getAll/', views.get_all, name='project_list'),
    path('api/create/', views.create, name='project_list'),
    path('api/getByIdPost/', views.get_by_id_post, name='project_list'),
    path('api/getByIdGet/<int:pk>', views.get_by_id_get, name='project_list'),
    path('api/put/<int:pk>', views.update, name='project_list'),

    path('', include(router.urls)),
]