from Lesson.lesson.responses.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def get_lesson_info_use_case(repo):
    return repo.list()

# def get_lesson_info_use_case(repo, request):
#     if not request:
#         return build_response_from_invalid_request(request)
#     try:
#         lesson_info = repo.list(filters=request.filters)
#         return ResponseSuccess(lesson_info)
#     except Exception as exc:
#         return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
