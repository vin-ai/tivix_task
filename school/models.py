from django.db import models
from django.utils.translation import gettext as _


class Teacher(models.Model):
    """A model class to manage all the teachers"""
    name = models.CharField(_('Name'), max_length=32)

    def __str__(self) -> str:
        return str(self.name)


class Student(models.Model):
    """A model class to manage all the students"""
    name = models.CharField(_('Name'), max_length=32)

    def __str__(self) -> str:
        return str(self.name)


class TeacherStudents(models.Model):
    """A model class to manage students association with
    a teacher that they teach"""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    star_student = models.BooleanField(default=False, db_index=True)

    class Meta:
        unique_together = (
            ('teacher', 'student'),
            ('teacher', 'student', 'star_student'),
        )

    def __str__(self) -> str:
        if self.star_student:
            return f'{self.teacher} - {self.student}*'
        return f'{self.teacher} - {self.student}'
