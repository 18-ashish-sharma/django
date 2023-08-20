from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [
    path('student-list/', views.student_list, name='student_data'),
    path('student-list-orm1/', views.student_list_ORM1, name='student_data_ORM1'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]