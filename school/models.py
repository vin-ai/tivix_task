from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Teacher(models.Model):
    """A model class to manage all the teachers"""
    name = models.CharField(_('Name'), max_length=32)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse("school:detail-teacher", kwargs={"pk": self.pk})


class Student(models.Model):
    """A model class to manage all the students"""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=32)
    star_student = models.BooleanField(default=False, db_index=True)

    def __str__(self) -> str:
        return str(self.name)
