#!/usr/bin/env python

from uuid import uuid4
from datetime import datetime

from Lesson.lesson.repository.lesson_group_repo import LessonGroupRepo
from Lesson.lesson.serializers.lesson_group import json_serial
from Lesson.lesson.use_cases.get_lesson_info import get_lesson_info_use_case
from Lesson.lesson.requests.lesson_group_list import build_lesson_group_list_request

lesson_groups = [
    {
        "group_id": uuid4(),
        "skill_level": 1,
        "student_limit": 20,
        "ski_slope_id": uuid4(),
        "price": 5.5,
        "language": "NL",
        "students": [
            {
                "student_id": uuid4(),
                "skill_level": 1,
                "booking_id": uuid4(),
                "confirmed": True,
                "language": "NL"
            },
            {
                "student_id": uuid4(),
                "skill_level": 1,
                "booking_id": uuid4(),
                "confirmed": False,
                "language": "NL"
            },
        ],
        "instructor": {
            "instructor_id": uuid4(),
            "skill_levels": [1, 2, 3],
            "languages": ["NL"]
        },
        "start_times": [json_serial(datetime.now())],
    },
]

request = build_lesson_group_list_request()
repo = LessonGroupRepo(lesson_groups)
response = get_lesson_info_use_case(repo, request)
print([lesson_group.to_dict() for lesson_group in response.value])
