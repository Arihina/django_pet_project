from django.contrib import admin

from .models import Parents, PersonalInfo, Direction, Teacher, Department, Group, Subject, Performance, TeacherSubject

# Register your models here.
admin.site.register(Parents)
admin.site.register(PersonalInfo)
admin.site.register(Direction)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Performance)
admin.site.register(TeacherSubject)
