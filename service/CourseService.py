from flask import request, make_response, jsonify

from models.course import Course


def api_course():
    courseservice = []
    for course in Course.objects:
        courseservice.append(course)
    return make_response(jsonify(courseservice), 200)


def api_coursep():
    content = request.json
    course = Course(course_id=content['course_id'],
                    course_name=content['course_name'],
                    instructor_id=content['instructor_id']

                    )
    course.save()
    return make_response("", 201)


def api_show_course(course_name):
    result3 = Course.objects(course_name=course_name)
    return result3.to_json()
