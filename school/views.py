from django.contrib import messages
from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import (View,
                                  ListView, FormView, UpdateView, DeleteView)
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
        teacher_name = form.cleaned_data['name']
        messages.add_message(self.request, messages.SUCCESS,
                             f'Teacher {teacher_name} Addedd Successfuly')
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


class TeacherDetailView(View):

    def get_object(self):
        try:
            # Fetch the requested teacher with all associated students
            # in once
            return Teacher.objects.prefetch_related('student_set') \
                .get(pk=self.kwargs['pk'])
        except Teacher.DoesNotExist as e:
            raise Http404() from e

    def get(self, request, *args, **kwargs):
        # get the teacher
        object = self.get_object()
        student_form = StudentForm(initial={'teacher': kwargs['pk']})

        context = {
            'object': object,
            'student_form': student_form
        }
        return render(request, 'school/teacher_detail.html',
                      context=context)

    def post(self, request, *args, **kwargs):
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_name = student_form.cleaned_data['name']
            student_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"Student {student_name} added successfuly")
            return HttpResponseRedirect(reverse('school:detail-teacher', kwargs=kwargs))

        # Render the same template as get() to show list/form with errors
        object = self.get_object()
        context = {
            'object': object,
            'student_form': student_form
        }
        return render(request, 'school/teacher_detail.html',
                      context=context)


class StudentListView(ListView):
    queryset = Student.objects.all()


class StudentFormView(FormView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_create.html'
    success_url = reverse_lazy('school:list-students')

    def form_valid(self, form):
        form.save()
        student_name = form.cleaned_data['name']
        messages.add_message(self.request, messages.SUCCESS,
                             f'Student {student_name} Addedd Successfuly')
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('name', 'teacher', 'star_student')
    template_name = 'school/student_update.html'

    def get_success_url(self):
        return reverse('school:list-students')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('school:list-students')
