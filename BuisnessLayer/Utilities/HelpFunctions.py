import json

def getSumOfData(historyDataList):
    sum = 0
    for d in historyDataList:
        Number1 = json.loads(d['data'])['number1']  
        Number2 = json.loads(d['data'])['number2']  
        sum = sum + Number1 + Number2
    return sum 
        
def formatTheResultForDB(sum):
    data = {'data': sum}
    data = json.dumps(data)
    return data         
    