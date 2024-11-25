from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')


def group(request):
    return redirect('home')


def study_info(request):
    pass


def department(request):
    pass


def personal_info(request):
    pass


def direction(request):
    pass


def teachers(request):
    pass


def parents(request):
    pass


def grade(request):
    pass
