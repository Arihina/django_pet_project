from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('teachers/', views.teachers, name='teachers'),
    path('groups/', views.groups, name='groups'),
    path('departments/', views.departments, name='departments'),
    path('performance/', views.performance, name='performance'),
    path('subjects/', views.subjects, name='subjects'),
    path('students/', views.students, name='students'),
]
