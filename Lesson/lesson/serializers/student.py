import json

class StudentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "student_id": str(o.student_id),
                "skill_level": str(o.skill_level),
                "booking_id": str(o.booking_id),
                "confirmed": str(o.confirmed),
                "language": json.dumps(o.language),
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
