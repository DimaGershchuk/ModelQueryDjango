from django.db.models import Avg, Count, Sum, Min, Max, F
from django.shortcuts import render
from .models import Teacher, ClassDetails, Student


def home_view(request):

    class_stats = ClassDetails.objects.annotate(
        average_age=Avg('student__age'),
        student_count=Count('student'),
        unigue_teacher=Count('teacher', distinct=True),
        total_attendance=Sum('student__attendance'),
    )

    overall_stats = Student.objects.aggregate(
        min_age=Min('age'),
        max_age=Max('age'),
        total_attendance=Sum('attendance'),
        average_attendance=Avg('attendance'),
    )

    adult_students = Student.objects.filter(age__gte=18)
    minor_students = Student.objects.filter(age__lt=18)

    overall_stats['adult_count'] = adult_students.count()
    overall_stats['minor_count'] = minor_students.count()

    overall_stats['adult_avg_attendance'] = adult_students.aggregate(avg=Avg('attendance'))['avg']
    overall_stats['minor_avg_attendance'] = minor_students.aggregate(avg=Avg('attendance'))['avg']

    students_above_avg_attendance = Student.objects.select_related('class_details').annotate(class_avg_attendance=Avg('class_details__student__attendance')).filter(attendance__gt=F('class_avg_attendance'))

    return render(request, 'home_page.html', {'class_stats': class_stats, 'overall_stats': overall_stats, 'students_above_avg_attendance': students_above_avg_attendance})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_detail.html', {'teachers': teachers})


def class_details_list(request):
    class_details = ClassDetails.objects.all()
    return render(request, 'class_detail.html', {'class_details': class_details})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_detail.html', {'students': students})



