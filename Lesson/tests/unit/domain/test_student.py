from Lesson.lesson.domain.student import Student
from Lesson.lesson.domain.language import Language

from uuid import uuid4
import unittest


class TestStudent(unittest.TestCase):
	def setUp(self) -> None:
		# Arrange for all tests
		self.student_id = uuid4()
		self.skill_level = 1
		self.booking_id = uuid4()
		self.confirmed = True
		self.language = Language.DE
		return super().setUp()


	def test_create_student(self):
		# Act
		student = Student(self.student_id, self.skill_level, self.booking_id, self.confirmed, self.language)

		# Assert
		assert student.student_id == self.student_id
		assert student.skill_level == self.skill_level
		assert student.booking_id == self.booking_id
		assert student.confirmed == self.confirmed
		assert student.language == self.language


	def test_create_student_from_dict(self):
		# Arrange
		student_dict = {
			"student_id": self.student_id,
			"skill_level": self.skill_level,
			"booking_id": self.booking_id,
			"confirmed": self.confirmed,
			"language": self.language.name
		}

		# Act
		student = Student.from_dict(student_dict)

		# Assert
		assert student.student_id == self.student_id
		assert student.skill_level == self.skill_level
		assert student.booking_id == self.booking_id
		assert student.confirmed == self.confirmed
		assert student.language == self.language


	def test_convert_student_to_dict(self):
		# Arrange
		student_dict = {
			"student_id": self.student_id,
			"skill_level": self.skill_level,
			"booking_id": self.booking_id,
			"confirmed": self.confirmed,
			"language": self.language.name
		}

		# Act
		student = Student.from_dict(student_dict)

		# Assert
		assert student.to_dict() == student_dict


	def test_compare_students(self):
		# Arrange
		student1 = Student(self.student_id, self.skill_level, self.booking_id, self.confirmed, self.language)
		student2 = Student(self.student_id, self.skill_level, self.booking_id, self.confirmed, self.language)

		# Act & Assert
		assert student1 == student2
