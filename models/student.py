from main import db


class Student(db.Document):
    student_id = db.IntField()
    student_name = db.StringField()
    city = db.StringField()
    program_id = db.IntField()
    semester_no = db.ListField()

    def to_json(self):
        return {
            "student_id ": self.student_id ,
            "student_name": self.student_name,
            "city": self.city,
            "program_id": self.program_id,
            "semester_no": self.semester_no
        }
