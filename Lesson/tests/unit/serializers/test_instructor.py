import json
import uuid

from Lesson.lesson.domain.instructor import Instructor
from Lesson.lesson.domain.language import Language
from Lesson.lesson.serializers.instructor import InstructorJsonEncoder


def test_serialize_domain_instructor():
    instructor_id = uuid.uuid4()
    skill_levels = [1,2,3,4]
    languages = [Language.DE, Language.NL]

    instructor = Instructor(
        instructor_id=instructor_id,
        skill_levels=skill_levels,
        languages=languages,
    )

    expected_json = f"""
        {{
            "instructor_id": "{instructor_id}",
            "skill_levels": {skill_levels},
            "languages": {json.dumps([language.name for language in languages])}
        }}
    """

    json_instructor = json.dumps(instructor, cls=InstructorJsonEncoder)
    assert json.loads(json_instructor) == json.loads(expected_json)
