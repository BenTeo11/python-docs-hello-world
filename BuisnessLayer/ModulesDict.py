from BuisnessLayer.Modules.SimpleMaths.SimpleMaths import SimpleMaths
from BuisnessLayer.Modules.SimpleMaths2.SimpleMaths2 import SimpleMaths2

theModules = {
  'SimpleMaths': SimpleMaths,
  'SimpleMaths2': SimpleMaths2
}

theInput_params = {
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