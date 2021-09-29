from graphene import relay, ObjectType
from graphene.types import mutation
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Teacher, Student


class TeacherNode(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = ("id", "name", "student_set")
        filter_fields = {
            "id": ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class StudentNode(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "star_student", "teacher")
        filter_fields = {
            "id": ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'star_student': ['exact'],
            'teacher': ['exact'],
            'teacher__name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    teacher = relay.Node.Field(TeacherNode)
    all_teachers = DjangoFilterConnectionField(TeacherNode)

    student = relay.Node.Field(StudentNode)
    all_students = DjangoFilterConnectionField(StudentNode)


class Mutation(ObjectType):
    pass
