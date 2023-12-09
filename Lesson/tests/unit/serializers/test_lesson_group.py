import json
import uuid
from datetime import datetime, date
import unittest

from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.domain.language import Language
from Lesson.lesson.domain.instructor import Instructor
from Lesson.lesson.domain.student import Student
from Lesson.lesson.serializers.lesson_group import LessonGroupJsonEncoder, json_serial
from Lesson.lesson.serializers.instructor import InstructorJsonEncoder
from Lesson.lesson.serializers.student import StudentJsonEncoder


def test_serialize_domain_lesson_group():
    group_id = uuid.uuid4()
    skill_level = 1
    student_limit = 20
    ski_slope_id = uuid.uuid4()
    price = 88.514
    language = Language.DE
    students = [Student(uuid.uuid4(), 1, uuid.uuid4(), True, Language.DE)]
    instructor = Instructor(uuid.uuid4(), [1], [Language.DE])
    start_times = [datetime.now(), datetime.now()]

    lesson_group = LessonGroup(
        group_id=group_id,
        skill_level=skill_level,
        student_limit=student_limit,
        ski_slope_id=ski_slope_id,
        price=price,
        language=language,
        students=students,
        instructor=instructor,
        start_times=start_times,
    )

    expected_json = f"""
        {{
            "group_id": "{group_id}",
            "skill_level": {skill_level},
            "student_limit": {student_limit},
            "ski_slope_id": "{ski_slope_id}",
            "price": {price},
            "language": "{language.name}",
            "students": {json.dumps(students, cls=StudentJsonEncoder)},
            "instructor": {json.dumps(instructor, cls=InstructorJsonEncoder)},
            "start_times": {json.dumps(start_times, default=json_serial)}
        }}
    """

    json_lesson_group = json.dumps(lesson_group, cls=LessonGroupJsonEncoder)
    assert json.loads(json_lesson_group) == json.loads(expected_json)
