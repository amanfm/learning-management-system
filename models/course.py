from main import db


class Course(db.Document):
    course_id = db.IntField()
    course_name = db.StringField()
    instructor_id = db.IntField()

    def to_json(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "instructor_id": self.instructor_id

        }
