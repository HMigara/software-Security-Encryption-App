import createKet
import testSQL
import HashingDB
import Hasinglogin
import DecryptionData
import EncryptionData
from flask import Flask,render_template,url_for,request

server =Flask(__name__)

@server.route("/")
def home():
    return render_template("home.html")

@server.route("/registation", methods=['GET','POST'])
def page():
     if request.method == "POST":
          form_data =  request.form
          print("form_DATA",form_data)
          password = form_data["password"]
          Email = form_data["Email"]
          userName = form_data["UserName"]
          role = form_data["inputState"]
          confirmpassword = form_data["confirmpw"]
          
          if password==confirmpassword:
               hashPww=HashingDB.hash_password(password)
               testSQL.registerUser(Email,userName,hashPww,role)
               return render_template("login.html")
          else:
                
                return "password not matched"
           
     return render_template("registation.html")          

   
 
@server.route("/login", methods=['GET','POST'])
def login():
     
     if request.method == "POST":
          form_data= request.form
          print("Form_data",form_data)
          Email = form_data["Email"]
          PW = form_data["password"]
          role = form_data ["inputState"]
          
          log =testSQL.loginUser(Email,PW,role)
          
          if log==True:
               msg =(DecryptionData.Decryption())
               return msg 
         
          
          
     return render_template("login.html")

@server.route("/home", methods= ['GET','POST'])
def message():
     if request.method=="POST":
          
          createKet.KeyGeneration()
          from_data = request.form
          message= from_data["msgfield"]
          print(message)
          EncryptionData.Encryption(message)
          
     return render_template("mesinterface.html")
  
server.run(debug=True)
