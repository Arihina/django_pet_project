from collections import defaultdict

from django.shortcuts import render

from .models import PersonalInfo, Department, TeacherSubject, Group


def index(request):
    return render(request, 'index.html')


def teachers(request):
    return render(request, 'teachers_menu.html')


def groups(request):
    all_info = PersonalInfo.objects.select_related('id_group__id_direction').all()
    d = defaultdict(list)

    for student in all_info:
        direction_long_name = student.get_direction_long_name()
        if direction_long_name:
            d[direction_long_name].append(student)

    d = dict(d)

    return render(request, 'groups.html', {'directions': d})


def departments(request):
    all_departments = Department.objects.prefetch_related('group_set').all()

    return render(request, 'departments.html', {'departments': all_departments})


def performance(request):
    students = PersonalInfo.objects.prefetch_related('performance_set').all()

    return render(request, 'performance.html', {'students': students})


def subjects(request):
    teacher_subjects = TeacherSubject.objects.select_related('id_teacher', 'id_subject').all()

    return render(request, 'teacher_subject.html', {'teacher_subjects': teacher_subjects})


def students(request):
    groups = Group.objects.prefetch_related('personalinfo_set').all()

    return render(request, 'students.html', {'groups': groups})


def put_exam(request):
    pass


def put_credit(request):
    pass
