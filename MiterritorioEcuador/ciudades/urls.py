from django.urls import path
from . import views

urlpatterns = [
    path('', views.ciudad_list, name='ciudad_list'),
    path('ciudad/<int:pk>/', views.ciudad_detail, name='ciudad_detail'),
    path('ciudad/nuevo/', views.ciudad_create, name='ciudad_create'),
    path('ciudad/<int:pk>/editar/', views.ciudad_update, name='ciudad_update'),
    path('ciudad/<int:pk>/eliminar/', views.ciudad_delete, name='ciudad_delete'),
]