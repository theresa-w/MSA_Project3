from app import app, db
from app.models import Diary

db.drop_all()
db.create_all()

dates = [
        "09-08-2020",
        "11-08-2020",
        "13-08-2020",
]

titles = [
    'saturday',
    'today',
    'happy day',
]


index = 0
for date in dates:
    new_task = Diary(date=date, title=titles[index], text='')
    db.session.add(new_task)
    index += 1

db.session.commit()
