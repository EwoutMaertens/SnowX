from flask import Flask

from .rest import lesson_group


def create_app(config_name):

    app = Flask(__name__)

    config_module = f"Lesson.lesson.application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(lesson_group.blueprint)

    return app