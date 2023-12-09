import json
import uuid
from datetime import datetime, date

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
    instructor = Instructor(uuid.uuid4(), 1, [Language.DE])
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
            "skill_level": "{skill_level}",
            "student_limit": "{student_limit}",
            "ski_slope_id": "{ski_slope_id}",
            "price": "{price}",
            "language": "{json.dumps(language)}",
            "students": {json.dumps(students, cls=StudentJsonEncoder)},
            "instructor": {json.dumps(instructor, cls=InstructorJsonEncoder)},
            "start_times": {json.dumps(start_times, default=json_serial)}
        }}
    """

    # TODO test fails:
    # {'group_id': 'f3f47890-14cf-49b8-8124-0fb30ee493e6', 'skill_level': '1', 'student_limit': '20', 'ski_slope_id': '08258edb-a802-4add-9635-c86bc3bd08e4', 'price': '88.514', 'language': '4', 'students': '[{"student_id": "e05bbf6f-bf11-4fac-8075-7e143e749205", "skill_level": "1", "booking_id": "22c56ed1-ae40-445b-857b-35a0e3dc8ba2", "confirmed": "True", "language": "4"}]', 'instructor': '{"instructor_id": "aa3fd3be-2d5f-40c3-88b0-666f9c883136", "skill_levels": "1", "languages": "[4]"}', 'start_times': '["2023-12-09T19:14:17.558568", "2023-12-09T19:14:17.558570"]'}

    # {'group_id': 'f3f47890-14cf-49b8-8124-0fb30ee493e6', 'skill_level': '1', 'student_limit': '20', 'ski_slope_id': '08258edb-a802-4add-9635-c86bc3bd08e4', 'price': '88.514', 'language': '4', 'students': [{'student_id': 'e05bbf6f-bf11-4fac-8075-7e143e749205', 'skill_level': '1', 'booking_id': '22c56ed1-ae40-445b-857b-35a0e3dc8ba2', 'confirmed': 'True', 'language': '4'}], 'instructor': {'instructor_id': 'aa3fd3be-2d5f-40c3-88b0-666f9c883136', 'skill_levels': '1', 'languages': '[4]'}, 'start_times': ['2023-12-09T19:14:17.558568', '2023-12-09T19:14:17.558570']}

    json_lesson_group = json.dumps(lesson_group, cls=LessonGroupJsonEncoder)
    assert json.loads(json_lesson_group) == json.loads(expected_json)
