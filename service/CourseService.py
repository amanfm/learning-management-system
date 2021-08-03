from flask import request, make_response, jsonify

from models.course import Course


def api_course():
    if request.method == "GET":
        courseservice = []
        for course in Course.objects:
            courseservice.append(course)
        return make_response(jsonify(courseservice), 200)
    elif request.method == "POST":
        content = request.json
        course = Course(course_id=content['course_id'],
                        course_name=content['course_name'],
                        instructor_id=content['instructor_id']

                        )
        course.save()
        return make_response("", 201)
