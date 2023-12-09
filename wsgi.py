import os

from Lesson.lesson.application.app import create_app

# This script will be automatically selected when running flask
# Usage: 'FLASK_CONFIG="development"  flask run'
# Then surf to 'http://127.0.0.1:5000/lesson_groups' to see results

app = create_app(os.environ["FLASK_CONFIG"])