import json
from uuid import uuid4
from datetime import datetime

from flask import Blueprint, Response, request
from Lesson.lesson.domain.language import Language

from Lesson.lesson.repository.lesson_group_repo import LessonGroupRepo
from Lesson.lesson.responses.responses import ResponseTypes
from Lesson.lesson.use_cases.get_lesson_info import get_lesson_info_use_case
from Lesson.lesson.serializers.lesson_group import LessonGroupJsonEncoder, json_serial
from Lesson.lesson.requests.lesson_group_list import build_lesson_group_list_request


blueprint = Blueprint("lesson_group", __name__)

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

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
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_object = build_lesson_group_list_request(
        filters=qrystr_params["filters"]
    )

    repo = LessonGroupRepo(lesson_groups_dict)
    response = get_lesson_info_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=LessonGroupJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )
