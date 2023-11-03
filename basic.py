# from flask import Flask, render_template

# app= Flask(__name__) ##creating an instance of a flask application


# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/puupy/<name>')
# def pup_name(name):
#     return render_template('puppy.html', name=name)

# if __name__=="__main__":
#     app.run(debug=True)

    
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
