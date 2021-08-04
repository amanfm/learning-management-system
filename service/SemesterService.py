from flask import request, make_response, jsonify

from models.semester import Semester


def api_sem():
    semesterservice = []
    for semester in Semester.objects:
        semesterservice.append(semester)
    return make_response(jsonify(semesterservice), 200)


def api_semp():
    content = request.json
    semester = Semester(sem_no=content['sem_no'],
                        sec_no=content['sec_no']
                        )
    semester.save()
    return make_response("", 201)


def api_show_semester(sem_no):
    result2 = Semester.objects(sem_no=sem_no)
    return result2.to_json()
