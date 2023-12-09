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
    def from_dict(self, instructor_dict):
        instructor = self(**instructor_dict)
        instructor.languages = [Language[language] for language in instructor.languages]
        return instructor

    def to_dict(self):
        instructor_dict = asdict(self)
        instructor_dict['languages'] = [language.name for language in instructor_dict['languages']]
        return instructor_dict
