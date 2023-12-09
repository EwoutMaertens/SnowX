import os

from Lesson.lesson.application.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])