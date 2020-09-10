from app import app, models
from flask import render_template

Diary = models.Diary

# http://www.website.com/
@app.route('/')
def index():
    entries = Diary.query.all()
    return render_template("index.html", entries = entries)