from django.test import TestCase
from .models import Teacher, Student, TeacherStudents


class Test_Create_Student(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_teacher = Teacher.objects.create(name='T-A')
        test_student_1 = Student.objects.create(name='S-a')
        test_teacher_student = TeacherStudents.objects.create(
            teacher=test_teacher,
            student=test_student_1
        )
        test_student_2 = Student.objects.create(name='S-b')
        test_teacher_star_student = TeacherStudents.objects.create(
            teacher=test_teacher,
            student=test_student_2,
            star_student=True
        )

    def test_teacher_student_content(self):
        """Tests that verifies the expected output
        from the model objects created above"""

        # Get the first teacher from DB
        teacher = Teacher.objects.get(pk=1)
        # Check whether it matches the expectd teacher name
        self.assertEqual(str(teacher), 'T-A')

        # Get the first student from DB
        student_1 = Student.objects.get(pk=1)
        # Check whether it matches the expectd student name
        self.assertEqual(str(student_1), 'S-a')

        # Get the first teacher and student association from DB
        teacher_student = TeacherStudents.objects.get(pk=1)
        # Match the expected output
        self.assertEqual(str(teacher_student), f'{teacher} - {student_1}')

        # Get the first student from DB
        student_2 = Student.objects.get(pk=2)
        # Check whether it matches the expectd student name
        self.assertEqual(str(student_2), 'S-b')

        # Get the first teacher and second student association from DB
        teacher_star_student = TeacherStudents.objects.get(pk=2)
        # Match the expected output
        self.assertEqual(str(teacher_star_student),
                         f'{teacher} - {student_2}*')
