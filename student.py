from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3'

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



# @app.route('/')
# def display_all():
#     return render_template('display_student.html', students=db.query.all())

if __name__== "__main__":
    app.run()
