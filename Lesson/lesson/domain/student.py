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
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return asdict(self)
	