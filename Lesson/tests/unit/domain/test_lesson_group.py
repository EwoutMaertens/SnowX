from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.domain.language import Language
from Lesson.lesson.domain.student import Student
from Lesson.lesson.domain.instructor import Instructor

from uuid import uuid4
from datetime import datetime
import unittest

from Lesson.lesson.serializers.lesson_group import json_serial

class TestLessonGroup(unittest.TestCase):
	def setUp(self) -> None:
		# Arrange for all tests
		self.group_id = uuid4()
		self.skill_level = 1
		self.student_limit = 20
		self.ski_slope_id = uuid4()
		self.price = 88.29
		self.language = Language.EN

		student1 = Student(uuid4(), 1, uuid4(), True, Language.EN)
		student2 = Student(uuid4(), 1, uuid4(), False, Language.EN)
		self.students = [student1, student2]
		self.instructor = Instructor(uuid4(), [1, 2], [Language.NL, Language.EN])
		self.start_times = [datetime.now(), datetime.now()]
		return super().setUp()


	def test_create_lesson_group(self):
		# Act
		lesson_group = LessonGroup(self.group_id, self.skill_level, self.student_limit,
		self.ski_slope_id, self.price, self.language, self.students,
		self.instructor, self.start_times)

		# Assert
		assert lesson_group.group_id == self.group_id
		assert lesson_group.skill_level == self.skill_level
		assert lesson_group.student_limit == self.student_limit
		assert lesson_group.ski_slope_id == self.ski_slope_id
		assert lesson_group.price == self.price
		assert lesson_group.language == self.language
		assert lesson_group.students == self.students
		assert lesson_group.instructor == self.instructor
		assert lesson_group.start_times == self.start_times


	def test_create_lesson_group_from_dict(self):
		# Arrange
		lesson_group_dict = {
			"group_id": self.group_id,
			"skill_level": self.skill_level,
			"student_limit": self.student_limit,
			"ski_slope_id": self.ski_slope_id,
			"price": self.price,
			"language": self.language.name,
			"students": [student.to_dict() for student in self.students],
			"instructor": self.instructor.to_dict(),
			"start_times": [json_serial(start_time) for start_time in self.start_times]
		}

		# Act
		lesson_group = LessonGroup.from_dict(lesson_group_dict)

		# Assert
		assert lesson_group.group_id == self.group_id
		assert lesson_group.skill_level == self.skill_level
		assert lesson_group.student_limit == self.student_limit
		assert lesson_group.ski_slope_id == self.ski_slope_id
		assert lesson_group.price == self.price
		assert lesson_group.language == self.language
		assert lesson_group.students == self.students
		assert lesson_group.instructor == self.instructor
		assert lesson_group.start_times == self.start_times


	def test_convert_lesson_group_to_dict(self):
		# Arrange
		lesson_group_dict = {
			"group_id": self.group_id,
			"skill_level": self.skill_level,
			"student_limit": self.student_limit,
			"ski_slope_id": self.ski_slope_id,
			"price": self.price,
			"language": self.language.name,
			"students": [student.to_dict() for student in self.students],
			"instructor": self.instructor.to_dict(),
			"start_times": [json_serial(start_time) for start_time in self.start_times]
		}

		# Act
		lesson_group = LessonGroup.from_dict(lesson_group_dict)

		# Assert
		assert lesson_group.to_dict() == lesson_group_dict


	def test_compare_lesson_groups(self):
		# Arrange
		lesson_group1 = LessonGroup(self.group_id, self.skill_level, self.student_limit,
								    self.ski_slope_id, self.price, self.language, self.students,
									self.instructor, self.start_times)
		lesson_group2 = LessonGroup(self.group_id, self.skill_level, self.student_limit,
									self.ski_slope_id, self.price, self.language, self.students,
									self.instructor, self.start_times)

		# Act & Assert
		assert lesson_group1 == lesson_group2
