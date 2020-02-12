from flask import Flask, jsonify, request, Response
import json
import jsonschema
#from jsonschema import validate, ValidationError, SchemaError
from BuisnessLayer.ModulesDict import *
from BuisnessLayer.Modules import * 

expected_keys = ['componentId' , 'destinationModule', 'data']

def validateData(data, response):
    if (validateInput(data,response)):
        return True
#input_data[in], response[out]
def validateInput(inputData, response):
    if not all (key in inputData for key in expected_keys):
        response = '\'componentId\' , \'destinationModule\', \'data\' should be included' , 400
        return False
     
    return True

#module[in] , data[in], theModuleObj[out], response[out]
def validateAndReturn_theModule(module, data, theModuleObj, response):
    found = False
    for moduleName,theModule in theModules.items():
        if (moduleName == module):
            found = True
            theModuleObj[0]  = theModule
            inputData_ref = theInput_params[moduleName]
            try:
                jsonschema.validate(data, inputData_ref)
            except jsonschema.ValidationError as jerr:
                response = str(jerr)
                return False
            except jsonschema.SchemaError as e:
                response = str(jerr)
                return False
            return True
    if (found == False):
        invalidDataObjectErrorMsg = {
            "error\":\"The Module selected to use, doesn't exist. Check the module list document.\n\""
            }
        response = invalidDataObjectErrorMsg
        return False

def extractInput(inputData):
    userInfo = inputData['componentId']
    module = inputData['destinationModule']
    data = json.dumps(inputData['data'])
    return userInfo,module,data

