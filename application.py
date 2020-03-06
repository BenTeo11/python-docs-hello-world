
from flask import Flask,jsonify, request, Response, render_template, session, redirect, url_for, flash
from flask_uuid import FlaskUUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy_utils import UUIDType
import json
import pyodbc
import urllib.parse
from uuid import uuid4
from BuisnessLayer.ModulesDict import *
from BuisnessLayer.Modules import * 
from DatabaseLayer.DataModel import *
from ApiLayer.Admin import *
from functools import wraps

import jwt,datetime

params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:apiservice.database.windows.net,1433;Database=ApiService;Uid=apiserviceAdmin;Pwd=BenTeo18062416;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

FlaskUUID(app)

app.config['SECRET_KEY'] = 'EdrMedeso2020' 
app.permanent_session_lifetime = datetime.timedelta(minutes=5)

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'] )
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.datetime.now()
    )
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"] 
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        password = request.form["pw"]        
        match = User.username_password_match(username, password)
        if match:
            session["user"] = username
            flash("Login Succesful!")
            session.permanent = True             
            return redirect(url_for("user"))
        else:
            flash("Invalid credentials!")
        return render_template("login.html")
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info") 
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/getToken', methods=['GET'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])
    
    match = User.username_password_match(username, password)
    
    if match:
        app.logger.info('%s logged in successfully',username)
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256' )
        return token
    else:
        return Response("",401,mimetype='application/json')


@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    if "user" in session:
        return render_template("home.html")
    else:
        flash("Please login to get access", "info") 
        return redirect(url_for("login"))

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/examples/")
def examples():
    return render_template("examples.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/view/")
def view():
    return render_template("view.html", values=User.getAllUsers())

@app.route('/GetData')
#@token_required
def get_data():
    token = request.args.get('token')
    try:
       jwt.decode(token, app.config['SECRET_KEY'] )
    except:
       return jsonify({'error': 'Need a valid token to view this page'}), 401
    return jsonify({'data': Data.get_all_data()})

@app.route('/GetDataByComponent')
#@token_required
def get_data_by_component():
    token = request.args.get('token')
    try:
       jwt.decode(token, app.config['SECRET_KEY'] )
    except:
       return jsonify({'error': 'Need a valid token to view this page'}), 401
    componentId = request.args.get('componentId') 
    componentId = componentId.strip('\"')
    return jsonify({'data': Result.get_data_by_id(componentId)})

@app.route('/GetDataByDevice')
#@token_required
def get_data_by_device():
    token = request.args.get('token')
    try:
       jwt.decode(token, app.config['SECRET_KEY'] )
    except:
       return jsonify({'error': 'Need a valid token to view this page'}), 401
    deviceId = request.args.get('deviceId') 
    return jsonify({'data': Device.get_data_by_id(deviceId)})

@app.route('/inputData', methods=['POST'])
def add_input():
    input_data = request.get_json()
    response = ''
    theModule =['']   
    if(validateData(input_data,response)):    
        userInfo,module,data = extractInput(input_data)           
        if(validateAndReturn_theModule(module, data, theModule, response)):
            timestamp = datetime.datetime.utcnow()    
            Data.add_data(timestamp, userInfo, data) 
            theModule[0](timestamp,userInfo,data)                   
            response = Response("",202,mimetype='application/json')
        return response
    else:
        invalidDataObjectErrorMsg = {
            "error\":\"Invalid data object passed in request\n\"",
            "helpString\":\"Data passed in similar to this{\"Bin1\": [75000,15418],\"Bin2\": [11100,32605]}"
            }
        response = Response(invalidDataObjectErrorMsg, status = 400, mimetype='application/json')
        return response


@app.route('/Create',methods=['PUT'])
def create():
    name = request.get_json()['name']
    #name = name['name']
    id = uuid4().hex
    Companies.insert(0,{id,name})
    print(Companies)
    if(validName(name)):
        #send name id to database
        response = Response(id, status=201,mimetype='application/json')
        return response
    

app.run(port=8000)

