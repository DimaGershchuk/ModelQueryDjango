from django.contrib import admin
from .models import Teacher, ClassDetails, Student, AdultStudent


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')


@admin.register(ClassDetails)
class ClassDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'class_details', 'attendance')


@admin.register(AdultStudent)
class AdultStudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'class_details', 'attendance')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(age__gte=18)
