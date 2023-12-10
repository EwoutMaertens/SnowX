from sqlalchemy import Column, Integer, String, Float, ARRAY, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LessonGroup(Base):
    __tablename__ = "lesson_group"

    id = Column(Integer, primary_key=True)

    group_id = Column(String(36), nullable=False)
    skill_level = Column(Integer)
    student_limit = Column(Integer)
    ski_slope_id = Column(String(36), nullable=False)
    price = Column(Float)
    language = Column(String(2))
    students = Column(ARRAY(String(36)))
    instructor = Column(String(36))
    start_times = Column(ARRAY(String(12)))


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)

    student_id = Column(String(36), nullable=False)
    skill_level = Column(Integer)
    booking_id = Column(String(36), nullable=False)
    confirmed = Column(Boolean)
    language = Column(String(2))


class Instructor(Base):
    __tablename__ = "instructor"

    id = Column(Integer, primary_key=True)

    instructor_id = Column(String(36), nullable=False)
    skill_levels = Column(ARRAY(Integer))
    languages = Column(ARRAY(String(2)))
