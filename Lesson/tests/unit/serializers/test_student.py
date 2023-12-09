import json
import uuid

from Lesson.lesson.domain.student import Student
from Lesson.lesson.domain.language import Language
from Lesson.lesson.serializers.student import StudentJsonEncoder


def test_serialize_domain_student():
    student_id = uuid.uuid4()
    skill_level = 1
    booking_id = uuid.uuid4()
    confirmed = True
    language = Language.DE

    student = Student(
        student_id=student_id,
        skill_level=skill_level,
        booking_id=booking_id,
        confirmed=confirmed,
        language=language,
    )

    expected_json = f"""
        {{
            "student_id": "{student_id}",
            "skill_level": "{skill_level}",
            "booking_id": "{booking_id}",
            "confirmed": "{confirmed}",
            "language": "{json.dumps(language)}"
        }}
    """

    json_student = json.dumps(student, cls=StudentJsonEncoder)
    assert json.loads(json_student) == json.loads(expected_json)
