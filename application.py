from flask import Flask,jsonify, request, Response
from flask_uuid import FlaskUUID
from uuid import uuid4
from DatabaseLayer.Settings import *
from DatabaseLayer.DataModel import *
from DatabaseLayer.UserModel import *
from BuisnessLayer.ModulesDict import *
from BuisnessLayer.Modules import * 
from ApiLayer.Admin import *
from functools import wraps


import jwt, datetime


FlaskUUID(app)

app.config['SECRET_KEY'] = 'EdrMedeso2020' 

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'] )
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper

@app.route('/login', methods=['POST'])
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


@app.route("/")
def hello():
    return "Welcome to EdrMedeso API Suite!"

def validData(data):
    return True

def validName(name):
    return True

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