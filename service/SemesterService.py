from flask import request, make_response, jsonify

from models.semester import Semester


def api_sem():
    if request.method == "GET":
        semesterservice = []
        for semester in Semester.objects:
            semesterservice.append(semester)
        return make_response(jsonify(semesterservice), 200)
    elif request.method == "POST":
        content = request.json
        semester = Semester(sem_no=content['sem_no'],
                            sec_no=content['sec_no']
                            )
        semester.save()
        return make_response("", 201)
