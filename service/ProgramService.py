from flask import request, make_response, jsonify

from models.program import Program


def api_program_get():
    programservice = []
    for program in Program.objects:
        programservice.append(program)
    return make_response(jsonify(programservice), 200)


def api_program_post():
    content = request.json
    program = Program(program_id=content['program_id'],
                      program_name=content['program_name'],
                      program_abbr=content['program_abbr']
                      )
    program.save()
    return make_response("", 201)


def api_show_program(program_abbr):
    result1 = Program.objects(program_abbr=program_abbr)
    return result1.to_json()
