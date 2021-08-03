from flask import request, make_response, jsonify

from models.instructor import Instructor


def api_instructor():
    if request.method == "GET":
        instructorservice = []
        for instructor in Instructor.objects:
            instructorservice.append(instructor)
        return make_response(jsonify(instructorservice), 200)
    elif request.method == "POST":
        content = request.json
        instructor = Instructor(instructor_id=content['instructor_id'],
                                instructor_name=content['instructor_name']
                                )
        instructor.save()
        return make_response("", 201)
