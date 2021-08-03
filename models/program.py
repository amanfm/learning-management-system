from main import db

PROGRAM_ID = ((1), (2), (3))

PROGRAM_NAME = (('Bachelor in business administration'),
                ('Bachelor of Engineering'), ('Bachelor In Management'))

PROGRAM_ABBR = (('BBA'), ('BE'), ('BIM'))

class Program(db.Document):
    program_id = db.IntField(choices=PROGRAM_ID)
    program_name = db.StringField(choices=PROGRAM_NAME)
    program_abbr = db.StringField(choices=PROGRAM_ABBR)

    def to_json(self):
        return {
            "program_id": self.program_id,
            "program_name": self.program_name,
            "program_abbr": self.program_abb
        }
