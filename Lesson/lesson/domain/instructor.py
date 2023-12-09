from uuid import UUID
from dataclasses import dataclass, asdict
from .language import Language
from typing import List

@dataclass
class Instructor():
    instructor_id: UUID
    skill_levels: List[int]
    languages: List[Language]

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return asdict(self)
