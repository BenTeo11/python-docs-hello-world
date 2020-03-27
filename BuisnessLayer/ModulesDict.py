from BuisnessLayer.Modules.SimpleMaths.SimpleMaths import SimpleMaths
from BuisnessLayer.Modules.SimpleMaths2.SimpleMaths2 import SimpleMaths2
from BuisnessLayer.Modules.WeldFat.WeldFat import *
from BuisnessLayer.Modules.BayesianInference.BayesianInference import *
#from BuisnessLayer.Modules.BayesianInference.BayesianTimeSeries import *


theModules = { 
  #"BayesianTimeSeriesAnalysis": BayesianTimeSeries,
  'BayesianInference': BayesianInference,
  'WeldFat':WeldFat,
  'SimpleMaths': SimpleMaths,
  'SimpleMaths2': SimpleMaths2
}


theInput_params = { "BayesianTimeSeriesAnalysis": {},
	'BayesianInference':{},
'WeldFat' : 
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  
  "properties": {
    "Method": {
      "type": "string",
      "enum": ["nominalFatigue"],
      	"title": "The Method Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": "",
				"examples": [
					"nominalFatigue"
				]
    },
    "fatClass": {
      "type": "array",
			"title": "The Fatclass Schema",
			"description": "An explanation about the purpose of this instance.",
			"default": [],
      "items": [
        {
          "type": "string",
          "enum": ['User Defined', 'IIW FAT160 steel', 'IIW FAT125 steel', 'IIW FAT112 steel', 'IIW FAT100 steel', 'IIW FAT90 steel', 'IIW FAT80 steel', 'IIW FAT71 steel', 'IIW FAT63 steel', 'IIW FAT56 steel', 'IIW FAT50 steel', 'IIW FAT45 steel', 'IIW FAT40 steel', 'IIW FAT36 steel', 'IIW FAT160 steel vari', 'IIW FAT125 steel vari', 'IIW FAT112 steel vari', 'IIW FAT100 steel vari', 'IIW FAT90 steel vari', 'IIW FAT80 steel vari', 'IIW FAT71 steel vari', 'IIW FAT63 steel vari', 'IIW FAT56 steel vari', 'IIW FAT50 steel vari', 'IIW FAT45 steel vari', 'IIW FAT40 steel vari', 'IIW FAT36 steel vari', 'IIW FAT71 aluminium', 'IIW FAT50 aluminium', 'IIW FAT45 aluminium', 'IIW FAT40 aluminium', 'IIW FAT36 aluminium', 'IIW FAT32 aluminium', 'IIW FAT28 aluminium', 'IIW FAT25 aluminium', 'IIW FAT22 aluminium', 'IIW FAT18 aluminium', 'IIW FAT16 aluminium', 'IIW FAT14 aluminium', 'IIW FAT12 aluminium', 'IIW FAT71 alu vari', 'IIW FAT50 alu vari', 'IIW FAT45 alu vari', 'IIW FAT40 alu vari', 'IIW FAT36 alu vari', 'IIW FAT32 alu vari', 'IIW FAT28 alu vari', 'IIW FAT25 alu vari', 'IIW FAT22 alu vari', 'IIW FAT18 alu vari', 'IIW FAT16 alu vari', 'IIW FAT14 alu vari', 'IIW FAT12 alu vari', 'IIW FAT225 R1 steel', 'IIW FAT71 R1 aluminium', 'IIW FAT28 R1 magnesium', 'IIW FAT630 R0.05 steel', 'IIW FAT180 R0.05 aluminium', 'IIW FAT71 R0.05 magnesium', 'IIW FAT225 R1 steel vari', 'IIW FAT71 R1 alu vari', 'IIW FAT28 R1 magn vari', 'IIW FAT630 R0.05 steel vari', 'IIW FAT180 R0.05 alu vari', 'IIW FAT71 R0.05 magn vari', 'DNV T.2-1 B1', 'DNV T.2-1 B2', 'DNV T.2-1 C', 'DNV T.2-1 C1', 'DNV T.2-1 C2', 'DNV T.2-1 D', 'DNV T.2-1 E', 'DNV T.2-1 F', 'DNV T.2-1 F1', 'DNV T.2-1 F3', 'DNV T.2-1 G', 'DNV T.2-1 W1', 'DNV T.2-1 W2', 'DNV T.2-1 W3', 'DNV T.2-1 T', 'DNV (2.4.6) Steel', 'DNV T.2-2 B1', 'DNV T.2-2 B2', 'DNV T.2-2 C', 'DNV T.2-2 C1', 'DNV T.2-2 C2', 'DNV T.2-2 D', 'DNV T.2-2 E', 'DNV T.2-2 F', 'DNV T.2-2 F1', 'DNV T.2-2 F3', 'DNV T.2-2 G', 'DNV T.2-2 W1', 'DNV T.2-2 W2', 'DNV T.2-2 W3', 'DNV T.2-2 T', 'DNV T.2-3 B1', 'DNV T.2-3 B2', 'DNV T.2-3 C', 'DNV T.2-3 C1', 'DNV T.2-3 C2', 'DNV T.2-3 D', 'DNV T.2-3 E', 'DNV T.2-3 F', 'DNV T.2-3 F1', 'DNV T.2-3 F3', 'DNV T.2-3 G', 'DNV T.2-3 W1', 'DNV T.2-3 W2', 'DNV T.2-3 W3', 'DNV T.2-3 T', 'EC3 FAT160', 'EC3 FAT140', 'EC3 FAT125', 'EC3 FAT112', 'EC3 FAT100', 'EC3 FAT90', 'EC3 FAT80', 'EC3 FAT71', 'EC3 FAT63', 'EC3 FAT56', 'EC3 FAT50', 'EC3 FAT45', 'EC3 FAT40', 'EC3 FAT36', 'EC3 FAT160 vari', 'EC3 FAT140 vari', 'EC3 FAT125 vari', 'EC3 FAT112 vari', 'EC3 FAT100 vari', 'EC3 FAT90 vari', 'EC3 FAT80 vari', 'EC3 FAT71 vari', 'EC3 FAT63 vari', 'EC3 FAT50 vari', 'EC3 FAT45 vari', 'EC3 FAT40 vari', 'EC3 FAT36 vari']
        },
        {
          "type": "number",
          "minimum": 0
        },
        {
          "type": "number",
          "minimum": 0
        },
        {
          "type": "number",
          "minimum": 0
        },
        {
          "type": "number",
          "minimum": 0
        },
        {
          "type": "number",
          "minimum": 0
        }
      ]
    },
    "meanStressTheory": {
      "type": "string",
      "enum": ["Goodman",'Gerber','Soderberg','None'],
      "title": "The Meanstresstheory Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": "",
				"examples": [
					"Goodman"
				]
    },
    "ultimateLimit": {
      "type": "number",
      "minimum": 0,
      "title": "The Ultimatelimit Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": 0,
				"examples": [
					500
				]
    },
    "yieldLimit": {
      "type": "number",
      "minimum": 0,
      "title": "The Yieldlimit Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": 0,
				"examples": [
					200
				]
    },
    "stressUnit": {
      "type": "string",
      "enum": ["pa","Pa","PA","mpa","Mpa","MPa","psi","Psi","PSI","ksi","Ksi","KSI"],
				"title": "The Stressunit Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": "",
				"examples": [
					"MPa"
				]},
    "Stress_Data": {
      "type": "object",
				"title": "The Stress_data Schema",
				"description": "An explanation about the purpose of this instance.",
				"default": {},
				"examples": [
					{
						"2": [
							0.20607635324664902,
							1.0,
							0.5865562435760306
						],
						"0": [
							0.11316419853821802,
							0.5,
							0.38605105361900416
						],
						"1": [
							0.4829431898813373,
							0.5,
							0.5709405492905638
						]
					}
				],
      "properties": {
        "/": {}
      },
    "patternProperties": {
        "^([0-9]+)+$": { "type": "array",
          "items": [
            {
              "type": "number"
            },
            {
              "type": "number"
            },
            {
              "type": "number"
            }
          ] }
    },
    "additionalProperties": False,
    }
  },
  "required": [
    "Method",
    "fatClass",
    "meanStressTheory",
    "ultimateLimit",
    "yieldLimit",
    "stressUnit",
    "Stress_Data"
  ]
},
	  'SimpleMaths': {
		  "type": "object",
		  "properties": {
			"number1": {
				"type": "number"
			},
			"number2":{
				"type":"number"
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

# from BuisnessLayer.Modules.SimpleMaths.SimpleMaths import SimpleMaths
# from BuisnessLayer.Modules.SimpleMaths2.SimpleMaths2 import SimpleMaths2
# from BuisnessLayer.Modules.WeldFat.WeldFat import *
# from BuisnessLayer.Modules.BayesianInference.BayesianInference import *

# theModules = {'BayesianInference': BayesianInference,
#   'WeldFat':WeldFat,
#   'SimpleMaths': SimpleMaths,
#   'SimpleMaths2': SimpleMaths2
# }

# theInput_params = {'BayesianInference':{},
# 	  'WeldFat' : {
#     	  "ultimateLimit": "float", 
#     	  "Stress_Data": {"dictionary"
#         	  }, 
#     	  "yieldLimit": "float", 
#     	  "fatClass": "string", 
#     	  "meanStressTheory": "string", 
#     	  "Method": "string"
# 	  },
# 	  'SimpleMaths': {
# 		  "type": "object",
# 		  "properties": {
# 			"number1": {
# 				"type": "number"
# 			},
# 			"number2":{	
# 				"type":"number"
# 		  }    
# 	  },
# 	  "required": [ "number1","number2"]
# 	},
# 	  'SimpleMaths2': {
# 			"type": "object",
# 			"properties": {
# 			  "number1": {
# 				"type": "integer"
# 			},
# 			"number2":{
# 				"type":"integer"
# 		  }    
# 	  },
# 	  "required": [ "number1","number2"]
# 	}
# } 