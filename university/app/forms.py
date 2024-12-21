from django import forms

from .models import Performance, Group, Teacher, Subject, Department, Direction


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['id_student', 'id_subject', 'Exam', 'Zachet']


class SearchForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=False, label='Полное имя')
    gender = forms.ChoiceField(choices=[
        ('', 'Все'),
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    ], required=False, label='Пол')


class InfoForm(forms.Form):
    parent_full_name = forms.CharField(label='ФИО Родителя', max_length=255)
    parent_phone_number = forms.CharField(label='Телефон Родителя', max_length=255)

    personal_full_name = forms.CharField(label='ФИО Студента', max_length=255)
    gender = forms.ChoiceField(label='Пол', choices=[('male', 'Мужской'), ('female', 'Женский')])
    birthday = forms.DateField(label='Дата Рождения', widget=forms.SelectDateWidget(years=range(1900, 2024)))
    phone_number = forms.CharField(label='Телефон Студента', max_length=255)
    address = forms.CharField(label='Адрес', max_length=255)
    id_group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Группа')


class TeacherForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Предметы'
    )

    class Meta:
        model = Teacher
        fields = ['full_name', 'Phone_number', 'subjects']
        labels = {
            'full_name': 'ФИО Преподавателя',
            'Phone_number': 'Телефон Преподавателя',
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        labels = {
            'name': 'Название Предмета',
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['id_direction', 'id_department', 'Year', 'Form', 'Degree']
        widgets = {
            'Year': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
            'Form': forms.TextInput(attrs={'placeholder': 'Например, Очная'}),
            'Degree': forms.TextInput(attrs={'placeholder': 'Например, Бакалавриат'}),
        }

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['id_direction'].queryset = Direction.objects.all()
        self.fields['id_department'].queryset = Department.objects.all()
