# from mongoengine import EmbeddedDocumentField

from main import db


# class Section(db.EmbeddedDocument):
#     section_no = db.IntField()


class Semester(db.Document):
    sem_no = db.IntField()
    sec_no = db.IntField()

    def to_json(self):
        return {
            "sem_no": self.sem_no,
            "sec_no": self.sec_no
        }
