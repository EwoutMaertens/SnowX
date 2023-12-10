from Lesson.lesson.domain.lesson_group import LessonGroup


class LessonGroupRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):

        result = [LessonGroup.from_dict(i) for i in self.data]

        if filters is None:
            return result

        if "student_limit__eq" in filters:
            result = [r for r in result if r.student_limit == filters["student_limit__eq"]]

        if "price__lt" in filters:
            result = [
                r for r in result if r.price < int(filters["price__lt"])
            ]

        if "price__gt" in filters:
            result = [
                r for r in result if r.price > int(filters["price__gt"])
            ]

        return result
