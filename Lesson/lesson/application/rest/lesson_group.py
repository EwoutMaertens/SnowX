import json
from uuid import uuid4
from datetime import datetime

from flask import Blueprint, Response
from Lesson.lesson.domain.language import Language

from Lesson.lesson.repository.lesson_group_repo import LessonGroupRepo
from Lesson.lesson.use_cases.get_lesson_info import get_lesson_info_use_case
from Lesson.lesson.serializers.lesson_group import LessonGroupJsonEncoder, json_serial

blueprint = Blueprint("lesson_group", __name__)

lesson_groups_dict = [
    {
        "group_id": str(uuid4()),
        "skill_level": 1,
        "student_limit": 20,
        "ski_slope_id": str(uuid4()),
        "price": 5.5,
        "language": Language.DE.name,
        "students": [
            {
                "student_id": str(uuid4()),
                "skill_level": 1,
                "booking_id": str(uuid4()),
                "confirmed": True,
                "language": Language.DE.name
            },
            {
                "student_id": str(uuid4()),
                "skill_level": 1,
                "booking_id": str(uuid4()),
                "confirmed": False,
                "language": Language.DE.name
            },
        ],
        "instructor": {
            "instructor_id": str(uuid4()),
            "skill_levels": [1, 2, 3],
            "languages": [Language.DE.name, Language.NL.name]
        },
        "start_times": [json_serial(datetime.now())],
    }
]

@blueprint.route("/lesson_groups", methods=["GET"])
def lesson_group_list():
    repo = LessonGroupRepo(lesson_groups_dict)
    result = get_lesson_info_use_case(repo)

    return Response(
        json.dumps(result, cls=LessonGroupJsonEncoder),
        mimetype="application/json",
        status=200,
    )
