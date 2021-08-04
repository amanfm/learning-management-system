from main import app
from service.CourseService import api_course, api_coursep, api_show_course
from service.InstructorService import api_instructor, api_instructorp, api_show_instructor
from service.ProgramService import api_program_get, api_program_post, api_show_program
from service.SemesterService import api_sem, api_semp, api_show_semester
from service.StudentService import api_student, api_studentp, api_show_student

app.add_url_rule("/api/program", "program", api_program_get, methods=['GET'])
app.add_url_rule("/api/programp", "programp", api_program_post, methods=['POST'])
app.add_url_rule("/api/program/<program_abbr>", "<program_abbr>", api_show_program)

app.add_url_rule("/api/semester", "semester", api_sem, methods=['GET'])
app.add_url_rule("/api/semesterp", "semesterp", api_semp, methods=['POST'])
app.add_url_rule("/api/semester/<sem_no>", "<sem_no>", api_show_semester)

app.add_url_rule("/api/course", "course", api_course, methods=['GET'])
app.add_url_rule("/api/coursep", "coursep", api_coursep, methods=['POST'])
app.add_url_rule("/api/course/<course_name>", "<course_name>", api_show_course)

app.add_url_rule("/api/instructor", "instructor", api_instructor, methods=['GET'])
app.add_url_rule("/api/instructorp", "instructorp", api_instructorp, methods=['POST'])
app.add_url_rule("/api/instructor/<instructor_name>", "<instructor_name>", api_show_instructor)

app.add_url_rule("/api/student", "student", api_student, methods=['GET'])
app.add_url_rule("/api/studentp", "studentp", api_studentp, methods=['POST'])
app.add_url_rule("/api/student/<student_name>", "<student_name>", api_show_student)

if __name__ == '__main__':
    app.run()
