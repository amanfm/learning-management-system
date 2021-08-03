from main import app
from service.CourseService import api_course
from service.InstructorService import api_instructor
from service.ProgramService import api_program
from service.SemesterService import api_sem
from service.StudentService import api_student

app.add_url_rule("/api/program", "program", api_program, methods=['GET', 'POST'])

app.add_url_rule("/api/semester", "semester", api_sem, methods=['GET', 'POST'])

app.add_url_rule("/api/course", "course", api_course, methods=['GET', 'POST'])

app.add_url_rule("/api/instructor", "instructor", api_instructor, methods=['GET', 'POST'])

app.add_url_rule("/api/student", "student", api_student, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()