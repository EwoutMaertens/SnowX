from Lesson.lesson.domain.lesson_group import LessonGroup


class LessonGroupRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        return [LessonGroup.from_dict(i) for i in self.data]
