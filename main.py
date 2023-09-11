from flask import Flask,render_template

server =Flask(__name__)

@server.route("/registation")
def page():
    return render_template("registation.html")
   
 
@server.route("/login")
def login():
     return render_template("login.html")

@server.route("/home")
def home():
     return render_template("mesinterface.html")
  
server.run(debug=True)
