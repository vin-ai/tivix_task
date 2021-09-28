from django.contrib import messages
from django.urls.base import reverse, reverse_lazy
from django.views.generic import (
    ListView, FormView, UpdateView, DeleteView, DetailView)
from .models import Teacher, Student
from .forms import StudentForm, TeacherForm


class TeacherListView(ListView):
    queryset = Teacher.objects.all()


class TeacherFormView(FormView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'school/teacher_create.html'
    success_url = reverse_lazy('school:list-teachers')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             'Teacher Addedd Successfuly')
        return super().form_valid(form)


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ('name',)
    template_name = 'school/teacher_update.html'

    def get_success_url(self):
        return reverse('school:detail-teacher', kwargs={'pk': self.object.id})


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('school:list-teachers')


class TeacherDetailView(DetailView):
    model = Teacher


class StudentListView(ListView):
    queryset = Student.objects.all()


class StudentFormView(FormView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_create.html'
    success_url = reverse_lazy('school:list-students')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             'Student Addedd Successfuly')
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('name', 'teacher', 'star_student')
    template_name = 'school/student_update.html'

    def get_success_url(self):
        return reverse('school:list-students')
