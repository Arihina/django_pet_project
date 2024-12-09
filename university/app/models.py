from django.db import models


class Parents(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Родители'
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    def __str__(self):
        return self.full_name


class PersonalInfo(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Birthday = models.DateField()
    Phone_number = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    id_parent = models.ForeignKey(Parents, on_delete=models.PROTECT, db_column='id_parent')
    id_group = models.ForeignKey('Group', on_delete=models.PROTECT, db_column='id_group')

    class Meta:
        db_table = 'Личная_информация'
        verbose_name = "Личная информация"
        verbose_name_plural = "Личная информация"

    def __str__(self):
        return self.full_name


class Direction(models.Model):
    id = models.AutoField(primary_key=True)
    Short_name = models.CharField(max_length=255)
    Long_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Направление'
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.Long_name


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Преподаватели'
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.full_name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, db_column='id_teacher')
    Short_name = models.CharField(max_length=255)
    Long_name = models.CharField(max_length=255)
    Decan = models.CharField(max_length=255)
    Phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'Кафедра'
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    def __str__(self):
        return self.Short_name


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    id_direction = models.ForeignKey(Direction, on_delete=models.PROTECT, db_column='id_napravlenie')
    id_department = models.ForeignKey(Department, on_delete=models.PROTECT, db_column='id_kafedra')
    Year = models.IntegerField()
    Form = models.CharField(max_length=255)
    Degree = models.CharField(max_length=255)

    class Meta:
        db_table = 'Группа'
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f'{self.id_department} {self.Year} ({self.Form} {self.Degree})'


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Предмет'
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class Performance(models.Model):
    id = models.AutoField(primary_key=True)
    id_student = models.ForeignKey(PersonalInfo, on_delete=models.PROTECT, db_column='id_student')
    id_subject = models.ForeignKey(Subject, on_delete=models.PROTECT, db_column='id_Object')
    Exam = models.IntegerField(null=True, blank=True)
    Zachet = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Успеваемость'
        verbose_name = "Успеваемость"
        verbose_name_plural = "Успеваемость"


class TeacherSubject(models.Model):
    id = models.AutoField(primary_key=True)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, db_column='id_teacher')
    id_subject = models.ForeignKey(Subject, on_delete=models.PROTECT, db_column='id_object')

    class Meta:
        db_table = 'Преподаватель_Предмет'
        verbose_name = "Преподаватель - Предмет"
        verbose_name_plural = "Преподаватели - Предметы"
