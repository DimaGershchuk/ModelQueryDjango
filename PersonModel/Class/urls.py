from django.urls import path
from .views import home_view, teacher_list, class_details_list, student_list


urlpatterns = [
    path('', home_view, name='home'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('classes/', class_details_list, name='class_details_list'),
    path('students/', student_list, name='student_list'),
]