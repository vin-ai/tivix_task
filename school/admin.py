from django.contrib import admin
from .models import Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('teacher',)
