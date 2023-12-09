import json

class InstructorJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "instructor_id": str(o.instructor_id),
                "skill_levels": json.dumps(o.skill_levels),
                "languages": json.dumps(o.languages),
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(o)
