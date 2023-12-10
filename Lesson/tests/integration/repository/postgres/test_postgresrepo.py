import pytest
from Lesson.lesson.repository import postgresrepo

pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_lesson_groups = repo.list()

    assert set([r.group_id for r in repo_lesson_groups]) == set(
        [r["group_id"] for r in pg_test_data]
    )


def test_repository_list_with_student_limit_equal_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_lesson_groups = repo.list(
        filters={"student_limit__eq": 20}
    )

    assert len(repo_lesson_groups) == 1
    assert repo_lesson_groups[0].student_limit == 20


def test_repository_list_with_price_less_than_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_lesson_groups = repo.list(filters={"price__lt": 60})

    assert len(repo_lesson_groups) == 1
    assert set([r.group_id for r in repo_lesson_groups]) == set(
        [r["group_id"] for r in pg_test_data]
    )


def test_repository_list_with_price_greater_than_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_lesson_groups = repo.list(filters={"price__gt": 48})

    assert len(repo_lesson_groups) == 1
    assert set([r.group_id for r in repo_lesson_groups]) == set(
        [r["group_id"] for r in pg_test_data]
    )


def test_repository_list_with_price_between_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_lesson_groups = repo.list(filters={"price__lt": 66, "price__gt": 48})

    assert len(repo_lesson_groups) == 1
    assert set([r.group_id for r in repo_lesson_groups]) == set(
        [r["group_id"] for r in pg_test_data]
    )
