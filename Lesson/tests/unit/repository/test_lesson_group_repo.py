import pytest
from uuid import uuid4
from datetime import datetime

from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.repository.lesson_group_repo import LessonGroupRepo
from Lesson.lesson.domain.language import Language
from Lesson.lesson.serializers.lesson_group import json_serial


@pytest.fixture
def lesson_group_dicts():
    return [
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


def test_repository_list_without_parameters(lesson_group_dicts):
    repo = LessonGroupRepo(lesson_group_dicts)

    lesson_groups = [LessonGroup.from_dict(i) for i in lesson_group_dicts]

    assert repo.list() == lesson_groups


def test_repository_list_with_student_limit_equal_filter(lesson_group_dicts):
    repo = LessonGroupRepo(lesson_group_dicts)

    lesson_groups = repo.list(
        filters={"student_limit__eq": 20}
    )

    assert len(lesson_groups) == 1
    assert lesson_groups[0].student_limit == 20


@pytest.mark.parametrize("price", [60, "60"])
def test_repository_list_with_price_less_than_filter(lesson_group_dicts, price):
    repo = LessonGroupRepo(lesson_group_dicts)

    lesson_groups = repo.list(filters={"price__lt": price})

    assert len(lesson_groups) == 1
    assert lesson_groups[0].price < float(price)


@pytest.mark.parametrize("price", [1, "4"])
def test_repository_list_with_price_greater_than_filter(lesson_group_dicts, price):
    repo = LessonGroupRepo(lesson_group_dicts)

    lesson_groups = repo.list(filters={"price__gt": price})

    assert len(lesson_groups) == 1
    assert lesson_groups[0].price > float(price)


def test_repository_list_with_price_between_filter(lesson_group_dicts):
    repo = LessonGroupRepo(lesson_group_dicts)

    lesson_groups = repo.list(filters={"price__lt": 30, "price__gt": 1})

    assert len(lesson_groups) == 1
    assert 1 < lesson_groups[0].price < 30
