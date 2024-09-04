from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Teacher(Person):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClassDetails(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Student(Person):
    class_details = models.ForeignKey(ClassDetails, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    attendance = models.PositiveIntegerField()


class AdultStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)


class AdultStudent(Student):
    objects = AdultStudentManager()

    class Meta:
        proxy = True

    def is_adult(self):
        return self.age >= 18





