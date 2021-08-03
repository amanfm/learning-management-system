from flask import request, make_response, jsonify

from models.program import Program


def api_program():
    if request.method == "GET":
        programservice = []
        for program in Program.objects:
            programservice.append(program)
        return make_response(jsonify(programservice), 200)
    elif request.method == "POST":
        content = request.json
        program = Program(program_id=content['program_id'],
                          program_name=content['program_name'],
                          program_abbr=content['program_abbr']
                          )
        program.save()
        return make_response("", 201)
