from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Lesson.lesson.domain.lesson_group import LessonGroup
from Lesson.lesson.domain.student import Student
from Lesson.lesson.domain.instructor import Instructor
from Lesson.lesson.domain.language import Language
from Lesson.lesson.repository import postgress_objects


class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        postgress_objects.Base.metadata.create_all(self.engine)
        postgress_objects.Base.metadata.bind = self.engine

    def _create_lesson_group_objects(self, results):
        return [
            LessonGroup(
                group_id=q.group_id,
                skill_level=q.skill_level,
                student_limit=q.student_limit,
                ski_slope_id=q.ski_slope_id,
                price=q.price,
                language=q.language,
                students=q.students,
                instructor=q.instructor,
                start_times=q.start_times
            )
            for q in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        query = session.query(postgress_objects.LessonGroup)

        if filters is None:
            return self._create_lesson_group_objects(query.all())

        if "student_limit__eq" in filters:
            query = query.filter(postgress_objects.LessonGroup.student_limit == filters["student_limit__eq"])

        if "price__lt" in filters:
            query = query.filter(postgress_objects.LessonGroup.price < filters["price__lt"])

        if "price__gt" in filters:
            query = query.filter(postgress_objects.LessonGroup.price > filters["price__gt"])

        return self._create_lesson_group_objects(query.all())
