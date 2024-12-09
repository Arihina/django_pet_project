from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('teachers/', views.teachers, name='teachers'),
    path('groups/', views.groups, name='groups'),
]
