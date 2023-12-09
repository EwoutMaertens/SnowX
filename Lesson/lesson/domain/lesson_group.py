from typing import List
from uuid import UUID
from dataclasses import dataclass, asdict
from datetime import datetime
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
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return asdict(self)