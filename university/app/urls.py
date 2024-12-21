from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('teachers/', views.teachers, name='teachers'),
    path('groups/', views.groups, name='groups'),
    path('departments/', views.departments, name='departments'),
    path('performance/', views.performance, name='performance'),
    path('students/', views.students, name='students'),
    path('subjects/', views.subjects, name='subjects'),
    path('add-subjects-mark/', views.add_subject_mark, name='add_subject_mark'),
    path('input-subject-id/', views.input_subject_id, name='input_subject_id'),
    path('upd-subjects-mark/<int:subject_id>/', views.update_subject_mark, name='update_subject_mark'),
    path('search-personal-info/', views.search_personal_info, name='search_personal_info'),
    path('login/', views.entrance, name='login'),
    path('add_personal_info/', views.add_personal_info, name='add_personal_info'),
]
