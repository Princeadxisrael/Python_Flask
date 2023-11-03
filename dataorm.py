from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///puppies.sqlite3"

db=SQLAlchemy(app)
app.app_context().push()

class Puppy(db.Model):
    __tablename__="puppies"
    id= db.Column('id', db.Integer, primary_key=True)
    name= db.Column( db.String)
    breed= db.Column( db.String)
    age= db.Column( db.Integer)
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age

    def __repr__(self):
        return f" This dog {self.name} is {self.age} years old"

@app.route('/')
def homepage():
    return "This is the Homepage"


if __name__== "__main__":
    app.run()




