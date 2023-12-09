#!/usr/bin/env python

from uuid import uuid4
from datetime import datetime

from Lesson.lesson.repository.lesson_group_repo import LessonGroupRepo
from Lesson.lesson.use_cases.get_lesson_info import get_lesson_info_use_case

lesson_groups = [
    {
        "group_id": uuid4(),
        "skill_level": 1,
        "student_limit": 20,
        "ski_slope_id": uuid4(),
        "price": 5.5,
        "language": 2,
        "students": [
            {
                "student_id": uuid4(),
                "skill_level": 1,
                "booking_id": uuid4(),
                "confirmed": True,
                "language": 2
            },
            {
                "student_id": uuid4(),
                "skill_level": 1,
                "booking_id": uuid4(),
                "confirmed": False,
                "language": 2
            },
        ],
        "instructor": {
            "instructor_id": uuid4(),
            "skill_levels": [1, 2, 3],
            "languages": [1, 2]
        },
        "start_times": [datetime.now()],
    },
]

repo = LessonGroupRepo(lesson_groups)
result = get_lesson_info_use_case(repo)
print(result)
