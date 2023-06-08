from django.db import models
from datetime import datetime






class Student(models.Model):
    first_name = models.CharField(max_length=50, default='Имя')
    last_name = models.CharField(max_length=50, default='Фамилия')
    phone = models.CharField(max_length=50, default='Номер')
    email = models.EmailField(max_length=50, default='Почта')
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")))
    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, default='Имя')
    last_name = models.CharField(max_length=50, default='Фамилия')
    phone = models.CharField(max_length=50, default='Номер')
    email = models.EmailField(max_length=50, default='Почта')
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")))

    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_level = models.CharField(max_length=50, choices=(("A1", "begginer"),("A2", "Elementary"), ("B1", "pre-intermedia"), ("B2", "Intermedia")))
    course_duration = models.IntegerField(choices=((2, "2 month"),(4, "4 months"), (6, "6 months"), (6, "6 months")))
    fee = models.FloatField(default=0)

    def __str__(self):
        return self.course_name


class Course_individual(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    members = models.IntegerField()




class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance_day = models.DateField(auto_now=True)
    attendance_status = models.CharField(max_length=50, choices=(("-", "absence"), ("+", "present")))

    def __str__(self):
        return self.attendance_status

class Assessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment = models.IntegerField()

    def __str__(self):
        return self.assessment



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=50, choices=(("2", "poor"),("3", "Satisfactory"), ("4", "good"), ("5", "excellent")))
    grade_day = models.DateField(auto_now=True)

    def __str__(self):
        return self.assessment

class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=50)
    material_description = models.TextField()
    material_link = models.CharField(max_length=200)

    def __str__(self):
        return self.material_name

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_per_week = models.CharField(max_length=50)
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.day_per_week

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50, default='Не выбран курс')
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    payment_amount = models.FloatField(default=0, verbose_name='Сумма платежа')


