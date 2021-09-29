import graphene
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
        interfaces = (graphene.relay.Node, )


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
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    teacher = graphene.relay.Node.Field(TeacherNode)
    all_teachers = DjangoFilterConnectionField(TeacherNode)

    student = graphene.relay.Node.Field(StudentNode)
    all_students = DjangoFilterConnectionField(StudentNode)


class TeacherMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    teacher = graphene.relay.Node.Field(TeacherNode)

    @classmethod
    def mutate(cls, root, info, name):
        teacher = Teacher(name=name)
        teacher.save()
        return cls(teacher=teacher)


class TeacherUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    teacher = graphene.relay.Node.Field(TeacherNode)

    @classmethod
    def mutate(cls, root, info, name, id):
        teacher = Teacher.objects.get(pk=id)
        teacher.name = name
        teacher.save()
        return cls(teacher=teacher)


class Mutation(graphene.ObjectType):
    add_teacher = TeacherMutation.Field()
    update_teacher = TeacherUpdate.Field()
