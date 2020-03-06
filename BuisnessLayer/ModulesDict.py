from BuisnessLayer.Modules.SimpleMaths.SimpleMaths import SimpleMaths
from BuisnessLayer.Modules.SimpleMaths2.SimpleMaths2 import SimpleMaths2
from BuisnessLayer.Modules.WeldFat.WeldFat import *
from BuisnessLayer.Modules.BayesianInference.BayesianInference import *

theModules = {'BayesianInference': BayesianInference,
  'WeldFat':WeldFat,
  'SimpleMaths': SimpleMaths,
  'SimpleMaths2': SimpleMaths2
}

theInput_params = {'BayesianInference':{},
	  'WeldFat' : {
    	  "ultimateLimit": "float", 
    	  "Stress_Data": {"dictionary"
        	  }, 
    	  "yieldLimit": "float", 
    	  "fatClass": "string", 
    	  "meanStressTheory": "string", 
    	  "Method": "string"
	  },
	  'SimpleMaths': {
		  "type": "string",
		  "properties": {
			"number1": {
				"type": "integer"
			},
			"number2":{
				"type":"integer"
		  }    
	  },
	  "required": [ "number1","number2"]
	},
	  'SimpleMaths2': {
			"type": "object",
			"properties": {
			  "number1": {
				"type": "integer"
			},
			"number2":{
				"type":"integer"
		  }    
	  },
	  "required": [ "number1","number2"]
	}
} 