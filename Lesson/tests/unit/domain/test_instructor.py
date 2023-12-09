from Lesson.lesson.domain.instructor import Instructor
from Lesson.lesson.domain.language import Language

from uuid import uuid4
import unittest


class TestInstructor(unittest.TestCase):
	def setUp(self) -> None:
		# Arrange for all tests
		self.instructor_id = uuid4()
		self.skill_levels = [1,2,3,4]
		self.languages = [Language.DE, Language.NL]
		return super().setUp()


	def test_create_instructor(self):
		# Act
		instructor = Instructor(self.instructor_id, self.skill_levels, self.languages)

		# Assert
		assert instructor.instructor_id == self.instructor_id
		assert instructor.skill_levels == self.skill_levels
		assert instructor.languages == self.languages


	def test_create_instructor_from_dict(self):
		# Arrange
		instructor_dict = {
			"instructor_id": self.instructor_id,
			"skill_levels": self.skill_levels,
			"languages": self.languages
		}

		# Act
		instructor = Instructor.from_dict(instructor_dict)

		# Assert
		assert instructor.instructor_id == self.instructor_id
		assert instructor.skill_levels == self.skill_levels
		assert instructor.languages == self.languages


	def test_convert_instructor_to_dict(self):
		# Arrange
		instructor_dict = {
			"instructor_id": self.instructor_id,
			"skill_levels": self.skill_levels,
			"languages": self.languages
		}

		# Act
		instructor = Instructor.from_dict(instructor_dict)

		# Assert
		assert instructor.to_dict() == instructor_dict


	def test_compare_instructors(self):
		# Arrange
		instructor1 = Instructor(self.instructor_id, self.skill_levels, self.languages)
		instructor2 = Instructor(self.instructor_id, self.skill_levels, self.languages)

		# Act & Assert
		assert instructor1 == instructor2
