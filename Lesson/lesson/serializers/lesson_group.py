import json
from datetime import datetime, date
from .instructor import InstructorJsonEncoder
from .student import StudentJsonEncoder


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


class LessonGroupJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "group_id": str(o.group_id),
                "skill_level": o.skill_level,
                "student_limit": o.student_limit,
                "ski_slope_id": str(o.ski_slope_id),
                "price": o.price,
                "language": o.language.name,
                "students": json.loads(json.dumps(o.students, cls=StudentJsonEncoder)),
                "instructor": json.loads(json.dumps(o.instructor, cls=InstructorJsonEncoder)),
                "start_times": json.loads(json.dumps(o.start_times, default=json_serial))
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
