from django.db import models


class Student(models.Model):

    class Meta:
        verbose_name_plural = "Student"
        db_table = "student"
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)


    @classmethod
    def create_student(cls, firstname, surname, age, classroom, teacher):
        student = cls(firstname=firstname, surname=surname, age=age, classroom=classroom, teacher=teacher)
        student.save()
        return student

    def __str__(self):
        return self.firstname



class Teacher(models.Model):

    class Meta:
        verbose_name_plural = "Teacher"
        db_table = "teacher"
      
    name = models.CharField(max_length=100)
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname