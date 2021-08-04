from flask import request, make_response, jsonify

from models.instructor import Instructor


def api_instructor():
    instructorservice = []
    for instructor in Instructor.objects:
        instructorservice.append(instructor)
    return make_response(jsonify(instructorservice), 200)


def api_instructorp():
    content = request.json
    instructor = Instructor(instructor_id=content['instructor_id'],
                            instructor_name=content['instructor_name']
                            )
    instructor.save()
    return make_response("", 201)


def api_show_instructor(instructor_name):
    result5 = Instructor.objects(instructor_name=instructor_name)
    return result5.to_json()
