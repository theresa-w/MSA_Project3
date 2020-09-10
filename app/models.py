from app import db
from datetime import datetime

# Models
class Diary(db.Model):
    date = db.Column(db.String(64), nullable=False, default=datetime.utcnow, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(1028))

    def __repr__(self):
        return '<Diary %r - ' % self.date, self.title, self.text

