from django.db import models


class Parents(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Родители'
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return self.full_name


class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Личная_информация'
        verbose_name = "Personal Info"
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.full_name


class Direction(models.Model):
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Направление'
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self):
        return self.short_name


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Преподаватели'
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.full_name


class Department(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    dean = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Кафедра'
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.short_name


class Group(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField()
    form = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)

    class Meta:
        db_table = 'Группа'
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Subject(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Предмет'
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Performance(models.Model):
    student = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.IntegerField(null=True, blank=True)
    credit = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Успеваемость'
        verbose_name = "Performance"
        verbose_name_plural = "Performances"


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Преподаватель_Предмет'
        verbose_name = "Teacher Subject"
        verbose_name_plural = "Teacher Subjects"
