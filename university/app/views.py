from collections import defaultdict

from django.shortcuts import render

from .models import PersonalInfo, Department


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
    departments = Department.objects.prefetch_related('group_set').all()

    return render(request, 'departments.html', {'departments': departments})
