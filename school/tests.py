from django.test import TestCase
from django.urls import reverse
from .models import Teacher, Student
from .forms import TeacherForm


class Test_Teacher_Views(TestCase):
    """
    Test all teacher views
    """

    def test_no_teachers(self):
        """
        Get teacher list must response 200 OK with empty list
        """
        url = reverse('school:list-teachers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No teachers yet.')
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_teacher_exists(self):
        """
        Teacher must exist in the html list and template context
        """
        # First feed data to DB
        teacher = Teacher.objects.create(name="Khushi Kalra")
        # Then test
        url = reverse('school:list-teachers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Khushi Kalra')
        self.assertQuerysetEqual(response.context['object_list'], [teacher])

    def test_teacher_form_valid(self):
        teacher_data = {
            'name': 'Khushi Kalra'
        }
        form = TeacherForm(teacher_data)
        self.assertTrue(form.is_valid())

    def test_teacher_form_invalid(self):
        teacher_data = {
            'name': 'Khushi Kalra asdfhasdfkjhasdfhasdhfkahsdfjahsdkfhaksldhfkasdhfkjhsdkjf'
        }
        form = TeacherForm(teacher_data)
        self.assertFalse(form.is_valid())
        expected_errors = {
            'name': [
                'Ensure this value has at most 32 characters (it has %d).' % len(
                    teacher_data.get('name'))
            ]
        }
        self.assertDictEqual(expected_errors, form.errors)

    def test_teacher_form_submits(self):
        teacher_data = {
            'name': 'Khushi Kalra'
        }
        response = self.client.post(
            reverse('school:create-teacher'), data=teacher_data)
        # Check if redirects on successful
        self.assertEqual(response.status_code, 302)


class Test_Create_Teacher(TestCase):

    @classmethod
    def setUpTestData(cls):
        Teacher.objects.create(name='T-A')

    def test_teacher_content(self):
        # Get the first teacher from DB
        teacher = Teacher.objects.get(pk=1)
        # Check whether it matches the expectd teacher name
        self.assertEqual(str(teacher), 'T-A')
        # Cgeck reverse url
        teacher_url = reverse("school:detail-teacher",
                              kwargs={"pk": teacher.id})
        self.assertEqual(teacher.get_absolute_url(), teacher_url)


class Test_Create_Student(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # Create a test teacher
        test_teacher = Teacher.objects.create(name='T-A')
        # create a student
        Student.objects.create(
            name='S-a',
            teacher=test_teacher
        )
        # create an another student with star grade for the teacher
        Student.objects.create(
            name='S-b',
            teacher=test_teacher,
            star_student=True
        )

    def test_teacher_student_content(self):
        """Tests that verifies the expected output
        from the model objects created above"""

        # Get the first student from DB
        student_1 = Student.objects.get(pk=1)
        # Check whether it matches the expectd student name
        self.assertEqual(str(student_1), 'S-a')
        self.assertEqual(str(student_1.teacher), 'T-A')

        # Get the first student from DB
        student_2 = Student.objects.get(pk=2)
        # Check whether it matches the expectd student name
        self.assertEqual(str(student_2), 'S-b')
        self.assertEqual(str(student_2.teacher), 'T-A')
        self.assertTrue(student_2.star_student)
