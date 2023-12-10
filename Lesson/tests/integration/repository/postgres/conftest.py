import sqlalchemy
import pytest
from datetime import datetime
from uuid import uuid4

from Lesson.lesson.domain.language import Language
from Lesson.lesson.repository.postgress_objects import Base, LessonGroup, Student, Instructor
from Lesson.lesson.serializers.lesson_group import json_serial


@pytest.fixture(scope="session")
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration["POSTGRES_USER"],
        app_configuration["POSTGRES_PASSWORD"],
        app_configuration["POSTGRES_HOSTNAME"],
        app_configuration["POSTGRES_PORT"],
        app_configuration["APPLICATION_DB"],
    )
    engine = sqlalchemy.create_engine(conn_str)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close


@pytest.fixture(scope="session")
def pg_test_data():
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


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    for r in pg_test_data:
        new_lesson_group = LessonGroup(
            group_id=r["group_id"],
            skill_level=r["skill_level"],
            student_limit=r["student_limit"],
            ski_slope_id=r["ski_slope_id"],
            price=r["price"],
            language=r["language"],
            students=[student["student_id"] for student in r["students"]],
            instructor=r["instructor"]["instructor_id"],
            start_times=r["start_times"]
        )
        pg_session_empty.add(new_lesson_group)

        for student in r["students"]:
            new_student = Student(
                student_id=student["student_id"],
                skill_level=student["skill_level"],
                booking_id=student["booking_id"],
                confirmed=student["confirmed"],
                language=student["language"]
            )
            pg_session_empty.add(new_student)

        new_instructor = Instructor(
            instructor_id=r["instructor"]["instructor_id"],
            skill_levels=r["instructor"]["skill_levels"],
            languages=r["instructor"]["languages"]
        )
        pg_session_empty.add(new_instructor)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(LessonGroup).delete()