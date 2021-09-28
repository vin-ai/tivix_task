from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'school'

urlpatterns = [
    path('', TemplateView.as_view(template_name='school/index.html'), name='home'),
    path('teachers/', views.TeacherListView.as_view(), name='list-teachers'),
    path('teachers/add/', views.TeacherFormView.as_view(), name='create-teacher'),
    path('teachers/<int:pk>/detail/',
         views.TeacherDetailView.as_view(), name='detail-teacher'),
    path('teachers/<int:pk>/update/',
         views.TeacherUpdateView.as_view(), name='update-teacher'),
    path('teachers/<int:pk>/delete/',
         views.TeacherDeleteView.as_view(), name='delete-teacher'),
    path('students/', views.StudentListView.as_view(), name='list-students'),
    path('students/add/', views.StudentFormView.as_view(), name='create-student'),
#     path('students/<int:pk>/detail/',
#          views.StudentListView.as_view(), name='detail-student'),
    path('students/<int:pk>/update/',
         views.StudentUpdateView.as_view(), name='update-student'),
    path('students/<int:pk>/delete/',
         views.StudentListView.as_view(), name='delete-student'),
]
