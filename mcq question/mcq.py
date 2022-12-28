from flask import Flask,render_template,request,redirect

import data.mcqutil as mcq_utils
file ="mcq question\studreg.json"
file1 = "mcq.json"
app=Flask(__name__)

@app.route("/", methods=["POST" , "GET"])

def index():
    return render_template("login.html")
@app.route("/login", methods= ["POST","GET"])
def login():
    data = mcq_utils.read_json(file)
    return render_template("mcq.html",data=data["student registration"])

@app.route("/register", methods=["POST" , "GET"])
def reg():
   
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        length=len(data["student registration"])
        fname=request.form["firstname"]
        lname=request.form["lastname"]
        date_of_birth= request.form["dob"]
        gender= request.form["inlineRadioOptions"]
        email= request.form["email"]
        username= request.form["username"]
        password= request.form["password"]
        list_of_stud={
            "s_no" : length+1,
            "Firstname" : fname,
            "Lastname"  : lname,
            "DOB" : date_of_birth,
            "Gender" : gender,
            "Email" : email,
            "Username" : username,
            "Password" : password,
        }
        data["student registration"].append(list_of_stud)
        mcq_utils.write_json(file,data)
        msg= username + " registration has been completed successfully !!"
        data = mcq_utils.read_json(file)
        return render_template("login.html",data=data["student registration"],msg=msg )
    return render_template("mcq2.html", data=data["student registration"])

@app.route("/dashboard", methods=["GET" , "POST"])
def dash():
    data = mcq_utils.read_json(file)
    message=""
    if request.method=="POST":                                                   
        email=request.form["Email"]
        password=request.form["Password"]
        message="your password or email incorrect"                   
        for i in data["student registration"] : 
            if i["Email"]==email :
                if i["Password"]==password:
                    return render_template("home.html", data=data["student registration"], email=email)
    return render_template("login.html" ,message=message)

@app.route("/caution", methods=["POST", "GET"])
def caution():
    return render_template("caution.html")  
@app.route("/caution2" , methods=["POST", "GET"])  
def cau():
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        passwrd=request.form["pasword"] 
        mesage="only owner / admin can open this section" 
        if passwrd=="rnaveen2520@":
            return render_template("mcq2.html",  data=data["student registration"]) 
        else:
            return render_template("caution.html",mesage=mesage)

@app.route("/forgot" , methods=["POST" , "GET"])  
def forgot():
    return render_template("forgot.html")

@app.route("/sentotp" , methods=["POST" , "GET"])
def otp():
    data = mcq_utils.read_json(file)
    num="0105"
    mes=""
    if request.method=="POST":
        email=request.form["email"]
        mes="your email id is incorrect / did not register / dont recognize"
        for i in data["student registration"] : 
            if i["Email"]==email:
                return render_template("otp.html", num=num)
    return render_template("forgot.html" , mes=mes)

       
      
    
if __name__=="__main__":
    app.run(debug=True)   