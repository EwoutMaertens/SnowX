from uuid import UUID
from dataclasses import dataclass, asdict
from .language import Language

@dataclass
class Student():
    student_id: UUID
    skill_level: int

    booking_id: UUID
    confirmed: bool

    language: Language

    @classmethod
    def from_dict(self, student_dict):
        student = self(**student_dict)
        student.language = Language[student.language]
        return student

    def to_dict(self):
        student_dict = asdict(self)
        student_dict['language'] = student_dict['language'].name
        return student_dict
	