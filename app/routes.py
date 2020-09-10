from app import app, models, db
from flask import render_template, request, redirect, url_for

Diary = models.Diary

# http://www.website.com/
@app.route('/')
def index():
    entries = Diary.query.all()
    return render_template("index.html", entries = entries)



# POST (Forms)
@app.route('/diary/', methods=['POST'])
def add_item():
    # Get data from form fields taskName and taskDescription
    diaryDate = request.form.get('diaryDate')
    diaryTitle = request.form.get('diaryTitle')
    diaryText = request.form.get('diaryText')
    
    # Put data into a new Task item
    new_entry = Diary(date=diaryDate, title=diaryTitle, text=diaryText)
    
    # Add and commit the changes to the database
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/diary/<date>', methods=['DELETE'])
def delete_task(date):
    entry = Diary.query.filter_by(date=date).first()
    
    # Check if Task exists
    if (entry != None):
        msg = {
            'message': 'Successful Delete'
        }
        db.session.delete(entry)
        db.session.commit()
        return jsonify(msg), 200
	
    # Task does not exist
    msg = {
        'message': 'No Entry found'
    }
    return jsonify(msg), 204