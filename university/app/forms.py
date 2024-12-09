from django import forms

from .models import Performance


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
