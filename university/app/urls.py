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
    path('add_subjects_mark/', views.add_subject_mark, name='add_subject_mark'),
    path('input_subject_id/', views.input_subject_id, name='input_subject_id'),
    path('upd_subjects_mark/<int:subject_id>/', views.update_subject_mark, name='update_subject_mark'),
    path('search_personal_info/', views.search_personal_info, name='search_personal_info'),
    path('login/', views.entrance, name='login'),
    path('login_dec/', views.login_dec, name='login_decv'),
    path('add_personal_info/', views.add_personal_info, name='add_personal_info'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_group/', views.add_group, name='add_group'),
    path('group_list/', views.group_list, name='group_list'),
    path('personal_info_list/', views.personal_info_list, name='personal_info_list'),
    path('login_dec/', views.login_dec, name='login_dec'),
    path('dean/', views.dean, name='dean'),
    path('personal_performance/', views.personal_performance, name='personal_performance'),
]
