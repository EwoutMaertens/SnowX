from typing import List
from uuid import UUID
from dataclasses import dataclass, asdict
from datetime import datetime

from Lesson.lesson.serializers.lesson_group import json_serial

from .student import Student
from .language import Language
from .instructor import Instructor

@dataclass
class LessonGroup():
    group_id: UUID
    skill_level: int
    student_limit: int

    ski_slope_id: UUID
    price: float

    language: Language
    students: List[Student]
    instructor: Instructor
    start_times: List[datetime]

    @classmethod
    def from_dict(self, lesson_group_dict):
        lesson_group = self(**lesson_group_dict)
        lesson_group.students = [Student.from_dict(student) for student in lesson_group.students]
        lesson_group.instructor = Instructor.from_dict(lesson_group.instructor)
        lesson_group.start_times = [datetime.fromisoformat(start_time) for start_time in lesson_group.start_times]
        lesson_group.language = Language[lesson_group.language]
        return lesson_group

    def to_dict(self):
        lesson_group_dict = asdict(self)
        lesson_group_dict['language'] = lesson_group_dict['language'].name
        lesson_group_dict['students'] = [student.to_dict() for student in self.students]
        lesson_group_dict['instructor'] = self.instructor.to_dict()
        lesson_group_dict['start_times'] = [json_serial(start_time) for start_time in self.start_times]
        return lesson_group_dict