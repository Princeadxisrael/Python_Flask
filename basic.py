from flask import Flask
app= Flask(__name__) ##creating an instance of a flask application



if __name__=="__main__":
    app.run(debug=True, port=8001)

    
# @app.route('/')
# def welcome():
#     return "<h1>Welcome</h1>"

# @app.route('/information')
# def info():
#     return "<h1> This is an information page<h1>"

# @app.route('/student/<name>')
# def student(name):
    
#     namestring=""
#     if name[-1]=="y":
#         namestring= name[:-1] + "iful"
#     else:
#         namestring= name + "y"
#     return "<h1> This user name is {} and the latin version is {}".format(name, namestring)
