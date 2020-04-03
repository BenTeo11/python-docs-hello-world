from flask import Flask, jsonify, request, Response
import json
import jsonschema
from BuisnessLayer.ModulesDict import *
from BuisnessLayer.Modules import * 

expected_keys = ['componentId' , 'destinationModule', 'data']

def validateData(data, response):
    if (validateInput(data,response)):
        return True
    
#input_data[in], response[out]
def validateInput(inputData, response):
    if not all (key in inputData for key in expected_keys):
        response[0] = '\'componentId\' , \'destinationModule\', \'data\' should be included in the json data'
        return False
     
    return True

#module[in] , data[in], theModuleObj[out], response[out]
def validateAndReturn_theModule(module, data, theModuleObj, response):
    found = False
    cerr  = ''
    for moduleName,theModule in theModules.items():
        if (moduleName == module):
            found = True
            theModuleObj[0]  = theModule
            inputData_ref = theInput_params[moduleName]
            try:
                data_dict=json.loads(data)
                jsonschema.validate(data_dict, inputData_ref)
            except jsonschema.ValidationError as jerr:
                response[0]  = str(jerr)
                return False
            except jsonschema.SchemaError as e:
                response[0]  = str(jerr)
                return False
                      
            cerr = validateContent(module,data)
            if(cerr != ''):
                response[0] = cerr
                return False
            
            return True
    if (found == False):
        invalidDataObjectErrorMsg = {
            "error\":\"The Module selected to use, doesn't exist. Check the module list document.\n\""
            }
        response[0] = invalidDataObjectErrorMsg
        return False

def extractInput(inputData):
    userInfo = inputData['componentId']
    module = inputData['destinationModule']
    data = json.dumps(inputData['data'])
    return userInfo,module,data

def validateContent(func, inputData):
    data = json.loads(inputData)
    errMsg = ''
    if(func == 'SimpleMaths'):
        if(data['number1'] < 10):
            errMsg = 'number1 is too low, try bigger number'
        elif(data['number1'] > 19):
            errMsg = 'number1 is too big, try smaller number'
        else:
            errMsg = ''
    return errMsg