import pytest
from uuid import uuid4
from unittest import mock
from datetime import datetime

from Lesson.lesson.domain.instructor import Instructor
from Lesson.lesson.domain.language import Language
from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.domain.student import Student
from Lesson.lesson.use_cases.get_lesson_info import get_lesson_info_use_case
from Lesson.lesson.requests.lesson_group_list import build_lesson_group_list_request
from Lesson.lesson.responses.responses import ResponseTypes


@pytest.fixture
def domain_lesson_groups():
    student1 = Student(uuid4(), 1, uuid4(), True, Language.EN)
    student2 = Student(uuid4(), 1, uuid4(), False, Language.EN)
    students = [student1, student2]
    instructor = Instructor(uuid4(), [1, 2], [Language.NL, Language.EN])
    start_times = [datetime.now(), datetime.now()]

    lesson_group_1 = LessonGroup(group_id=uuid4(), skill_level=1, student_limit=20,
                                 ski_slope_id=uuid4(), price=10, language=Language.EN, students=students,
                                 instructor=instructor, start_times=start_times)
    lesson_group_2 = LessonGroup(group_id=uuid4(), skill_level=2, student_limit=20,
                                 ski_slope_id=uuid4(), price=20, language=Language.EN, students=students,
                                 instructor=instructor, start_times=start_times)
    lesson_group_3 = LessonGroup(group_id=uuid4(), skill_level=3, student_limit=10,
                                 ski_slope_id=uuid4(), price=30, language=Language.DE, students=students,
                                 instructor=instructor, start_times=start_times)
    lesson_group_4 = LessonGroup(group_id=uuid4(), skill_level=4, student_limit=10,
                                 ski_slope_id=uuid4(), price=40, language=Language.DE, students=students,
                                 instructor=instructor, start_times=start_times)


    return [lesson_group_1, lesson_group_2, lesson_group_3, lesson_group_4]


def test_lesson_group_list_without_parameters(domain_lesson_groups):
    repo = mock.Mock()
    repo.list.return_value = domain_lesson_groups

    request = build_lesson_group_list_request()

    response = get_lesson_info_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_lesson_groups


def test_lesson_group_list_with_filters(domain_lesson_groups):
    repo = mock.Mock()
    repo.list.return_value = domain_lesson_groups

    qry_filters = {"student_limit__eq": 10}
    request = build_lesson_group_list_request(filters=qry_filters)

    response = get_lesson_info_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_lesson_groups


def test_lesson_group_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_lesson_group_list_request(filters={})

    response = get_lesson_info_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_lesson_group_list_handles_bad_request():
    repo = mock.Mock()

    request = build_lesson_group_list_request(filters=5)

    response = get_lesson_info_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }