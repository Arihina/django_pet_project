from collections import defaultdict

from django.shortcuts import render, redirect, get_object_or_404

from .forms import PerformanceForm, SearchForm
from .models import PersonalInfo, Department, TeacherSubject, Group, Performance


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


def add_subject_mark(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PerformanceForm()

    return render(request, 'add_performance.html', {'form': form})


def input_subject_id(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        return redirect('update_subject_mark', subject_id=subject_id)

    return render(request, 'input_subject_id.html')


def update_subject_mark(request, subject_id):
    subject = get_object_or_404(Performance, id=subject_id)

    if request.method == 'POST':
        exam = request.POST.get('exam_mark')
        credit = request.POST.get('credit_mark')

        if exam:
            subject.Exam = exam
        if credit:
            subject.Zachet = credit

        subject.save()

    context = {
        'subject': subject
    }
    return render(request, 'update_subject_mark.html', context)


def search_personal_info(request):
    form = SearchForm(request.GET or None)
    results = PersonalInfo.objects.all()

    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        gender = form.cleaned_data.get('gender')

        if full_name:
            results = results.filter(full_name__icontains=full_name)
        if gender:
            results = results.filter(Gender=gender)

    context = {
        'form': form,
        'results': results
    }
    return render(request, 'search_personal_info.html', context)


def entrance(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        if password == 'admin':
            return redirect('teachers')
        else:
            error_message = "Неверный пароль"
            return render(request, 'password_check.html', {'error_message': error_message})

    return render(request, 'entrance.html')
