from main import db


class Instructor(db.Document):
    instructor_id = db.IntField()
    instructor_name = db.StringField()

    def to_json(self):
        return {
            "instructor_id": self.instructor_id,
            "instructor_name": self.instructor_name,

        }