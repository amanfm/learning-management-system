from main import db
# from models.semester import Semester


class Student(db.Document):
    student_id = db.IntField()
    student_name = db.StringField()
    city = db.StringField()
    program_id = db.IntField()
    sem_no = db.ListField()

    def to_json(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "city": self.city,
            "program_id": self.program_id,
            "sem_no": self.sem_no
        }
