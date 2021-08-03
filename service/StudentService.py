from flask import request, make_response, jsonify

from models.student import Student


def api_student():
    if request.method == "GET":
        studentservice = []
        for student in Student.objects:
            student.append(student)
        return make_response(jsonify(studentservice), 200)
    elif request.method == "POST":
        content = request.json
        student = Student(student_id=content['student_id'],
                          student_name=content['student_name'],
                          city=content['city'],
                          program_id=content['program_id'],
                          semester_no=content['semester_no']
                          )
        student.save()
        return make_response("", 201)
