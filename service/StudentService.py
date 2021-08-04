from flask import request, make_response, jsonify

from models.student import Student


def api_student():
    studentservice = []
    for student in Student.objects:
        studentservice.append(student)
    return make_response(jsonify(studentservice), 200)


def api_studentp():
    content = request.json
    student = Student(student_id=content['student_id'],
                      student_name=content['student_name'],
                      city=content['city'],
                      program_id=content['program_id'],
                      sem_no=content['sem_no']
                      )
    student.save()
    return make_response("", 201)


def api_show_student(student_name):
    result6 = Student.objects(student_name=student_name)
    return result6.to_json()
