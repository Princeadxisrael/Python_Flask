from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3'
app.config['SECRET_KEY']="random string"

db=SQLAlchemy(app)
app.app_context().push()


# migrate=Migrate(app, db)


class Students (db.Model):
    __tablename__="students"
    id=db.Column('student_id', db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    city=db.Column(db.String(50))
    addr=db.Column(db.String(200))
    pin=db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin
    def __repr__(self):
        return f"Student {self.name} is from {self.city} and has a pin{self.pin}"
@app.route('/')
def displayall():
    return render_template('display_student.html', students=Students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method=='POST':
        if not request.form['name'] or not request.form['city'] or not request.form['city']or not request.form['addr']:
            flash('Please enter all fields', 'error')
        else:
            student=Students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('record was successfully added to db')
            return redirect(url_for('displayall'))
    return render_template('new.html')
if __name__== "__main__":
    app.run(debug=True)



