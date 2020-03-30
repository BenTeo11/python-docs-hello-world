from flask import Flask,jsonify, request, Response
import json
import uuid
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *

def SimpleMaths(timestamp,_componentId, jsonInput,response):  
    #retrieve the last 3 entries from the 'Data' table from the database for the given component 
    try:  
        historyDataList = Data.get_data_the_lastrows(3,_componentId)
    except:
        response[0] = 'reading history failed.'
    
    sum = getSumOfData(historyDataList)
      
    #insert the result to the 'Result' database
    data = formatTheResultForDB(sum)

    #_resultTimeStamp = datetime.datetime.utcnow()
    Result.add_data(timestamp, datetime.datetime.utcnow() , _componentId, data)

