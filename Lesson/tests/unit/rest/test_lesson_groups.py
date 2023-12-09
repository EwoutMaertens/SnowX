import json
from unittest import mock
from uuid import uuid4
from datetime import datetime

from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.serializers.lesson_group import json_serial
from Lesson.lesson.domain.language import Language


lesson_groups_dict = {
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

lesson_groups = [LessonGroup.from_dict(lesson_groups_dict)]


@mock.patch("Lesson.lesson.application.rest.lesson_group.get_lesson_info_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = lesson_groups

    http_response = client.get("/lesson_groups")

    assert json.loads(http_response.data.decode("UTF-8")) == [lesson_groups_dict]
    mock_use_case.assert_called_once()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
