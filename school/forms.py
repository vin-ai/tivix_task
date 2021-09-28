from django import forms
from django.forms import widgets
from .models import Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('teacher', 'name', 'star_student')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'star_student': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'teacher': forms.Select(attrs={'class': 'form-select'})
        }
