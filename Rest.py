from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)

api=Api(app)

students=[]

class Welcome(Resource):
    def get(self):
        return {'Welcome': 'User'}
    
class studentinfo(Resource):
    def get (self,name):
        for student in students:
            if student["name"]==name:
                return student
        return {"name": None}
    def post(self, name):
        student={'name': name}
        students.append(student)
        return {"message": "Successfully added"}

    def delete(self,name):
        for index, student in enumerate(students):
            if student["name"]==name:
                students.pop(index)
                return {"prompt": "Succesfully deleted"}
            
class allstudents(Resource):
    def get(self):
        return {"students": students}

api.add_resource(Welcome, '/')
api.add_resource (studentinfo, '/student/<string:name>')
api.add_resource (allstudents, '/students')


if  __name__=="__main__":
    app.run(debug=True)
