from collections import defaultdict

from django.shortcuts import render, redirect, get_object_or_404

from .forms import SearchForm, InfoForm, TeacherForm, SubjectForm, GroupForm, StudentPerformanceForm, NewPerformanceForm
from .models import PersonalInfo, Department, TeacherSubject, Group, Performance, Parents, Subject


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
    form = NewPerformanceForm()
    students = None
    if request.method == 'POST':
        if 'save_performance' in request.POST:
            subject = Subject.objects.get(id=request.POST['subject'])
            for student_id in request.POST.getlist('student_ids'):
                zachet = request.POST.get(f'zachet_{student_id}', '')
                exam = request.POST.get(f'exam_{student_id}', '')

                student = PersonalInfo.objects.get(id=student_id)

                Performance.objects.update_or_create(
                    id_student=student,
                    id_subject=subject,
                    defaults={
                        'Zachet': zachet if zachet else None,
                        'Exam': exam if exam else None
                    }
                )
        elif 'group' in request.POST and 'subject' in request.POST:
            group_id = request.POST['group']
            subject_id = request.POST['subject']
            group = Group.objects.get(id=group_id)
            subject = Subject.objects.get(id=subject_id)

            students = PersonalInfo.objects.filter(id_group=group)

            form = NewPerformanceForm(initial={'group': group,
                                               'subject': subject})

            return render(request, 'set_performance.html', {
                'form': form,
                'students': students,
                'subject': subject,
                'group': group
            })

    return render(request, 'set_performance.html', {'form': form, 'students': students})


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


def add_personal_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)

        if form.is_valid():
            parent = Parents.objects.create(
                full_name=form.cleaned_data['parent_full_name'],
                Phone_number=form.cleaned_data['parent_phone_number']
            )

            PersonalInfo.objects.create(
                full_name=form.cleaned_data['personal_full_name'],
                Gender=form.cleaned_data['gender'],
                Birthday=form.cleaned_data['birthday'],
                Phone_number=form.cleaned_data['phone_number'],
                Address=form.cleaned_data['address'],
                id_parent=parent,
                id_group=form.cleaned_data['id_group']
            )

    else:
        form = InfoForm()

    return render(request, 'add_personal_info.html', {'form': form})


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            subjects = form.cleaned_data['subjects']

            for subject in subjects:
                TeacherSubject.objects.create(id_teacher=teacher, id_subject=subject)

    else:
        form = TeacherForm()

    return render(request, 'add_teacher.html', {'form': form})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubjectForm()

    return render(request, 'add_subject.html', {'form': form})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GroupForm()

    return render(request, 'add_group.html', {'form': form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})


def personal_info_list(request):
    personal_info = PersonalInfo.objects.all()
    return render(request, 'personal_info_list.html', {'personal_info': personal_info})


def login_dec(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        if password == 'admin':
            return redirect('dean')
        else:
            error_message = "Неверный пароль"
            return render(request, 'password_check.html', {'error_message': error_message})

    return render(request, 'entrance.html')


def dean(request):
    return render(request, 'dean_menu.html')


def personal_performance(request):
    form = StudentPerformanceForm()
    performances = None

    if request.method == 'POST':
        form = StudentPerformanceForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            try:
                performances = Performance.objects.filter(id_student__id=student_id)
            except PersonalInfo.DoesNotExist:
                performances = None

    return render(request, 'performance_info.html', {'form': form, 'performances': performances})
