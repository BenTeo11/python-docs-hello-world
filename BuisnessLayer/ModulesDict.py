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
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "title": "The Weld Fatigue Root Schema",
    "description": "The root schema comprises the entire JSON document.",
    "required": [
        "method",
        "fatigue_class",
        "stress_unit"
    ],
    "properties": {
        "method": {
            "type": "string",
            "enum": ["Nominal Fatigue"],
            "title": "The method Schema",
            "description": "Specify the Weld Fatigue method based on the IIW recommendations",
            "examples": [
                "Nominal Fatigue"
            ]
        },
        "fatigue_class": {
            "type": "object",
            "title": "The fatigue_class Schema",
            "description": "Define S-N curves to be used.",
            "examples": [
                {
                    "n_c": 10000000.0,
                    "fat_fact": 1.0,
                    "fat": 100.0,
                    "m_1": 5.0,
                    "m_2": 22.0,
                    "class": "User defined",
                    "n_fat": 2000000.0
                }
            ],
            "properties": {
                "class": {
                    "type": "string",
                    "enum": ["IIW FAT160 steel", "IIW FAT125 steel", "IIW FAT112 steel", "IIW FAT100 steel", "IIW FAT90 steel", "IIW FAT80 steel", "IIW FAT71 steel", "IIW FAT63 steel", "IIW FAT56 steel", "IIW FAT50 steel", "IIW FAT45 steel", "IIW FAT40 steel", "IIW FAT36 steel", "IIW FAT160 steel vari", "IIW FAT125 steel vari", "IIW FAT112 steel vari", "IIW FAT100 steel vari", "IIW FAT90 steel vari", "IIW FAT80 steel vari", "IIW FAT71 steel vari", "IIW FAT63 steel vari", "IIW FAT56 steel vari", "IIW FAT50 steel vari", "IIW FAT45 steel vari", "IIW FAT40 steel vari", "IIW FAT36 steel vari", "IIW FAT71 aluminium", "IIW FAT50 aluminium", "IIW FAT45 aluminium", "IIW FAT40 aluminium", "IIW FAT36 aluminium", "IIW FAT32 aluminium", "IIW FAT28 aluminium", "IIW FAT25 aluminium", "IIW FAT22 aluminium", "IIW FAT18 aluminium", "IIW FAT16 aluminium", "IIW FAT14 aluminium", "IIW FAT12 aluminium", "IIW FAT71 alu vari", "IIW FAT50 alu vari", "IIW FAT45 alu vari", "IIW FAT40 alu vari", "IIW FAT36 alu vari", "IIW FAT32 alu vari", "IIW FAT28 alu vari", "IIW FAT25 alu vari", "IIW FAT22 alu vari", "IIW FAT18 alu vari", "IIW FAT16 alu vari", "IIW FAT14 alu vari", "IIW FAT12 alu vari", "IIW FAT225 R1 steel", "IIW FAT71 R1 aluminium", "IIW FAT28 R1 magnesium", "IIW FAT630 R0.05 steel", "IIW FAT180 R0.05 aluminium", "IIW FAT71 R0.05 magnesium", "IIW FAT225 R1 steel vari", "IIW FAT71 R1 alu vari", "IIW FAT28 R1 magn vari", "IIW FAT630 R0.05 steel vari", "IIW FAT180 R0.05 alu vari", "IIW FAT71 R0.05 magn vari", "DNV T.2-1 B1", "DNV T.2-1 B2", "DNV T.2-1 C", "DNV T.2-1 C1", "DNV T.2-1 C2", "DNV T.2-1 D", "DNV T.2-1 E", "DNV T.2-1 F", "DNV T.2-1 F1", "DNV T.2-1 F3", "DNV T.2-1 G", "DNV T.2-1 W1", "DNV T.2-1 W2", "DNV T.2-1 W3", "DNV T.2-1 T", "DNV (2.4.6) Steel", "DNV T.2-2 B1", "DNV T.2-2 B2", "DNV T.2-2 C", "DNV T.2-2 C1", "DNV T.2-2 C2", "DNV T.2-2 D", "DNV T.2-2 E", "DNV T.2-2 F", "DNV T.2-2 F1", "DNV T.2-2 F3", "DNV T.2-2 G", "DNV T.2-2 W1", "DNV T.2-2 W2", "DNV T.2-2 W3", "DNV T.2-2 T", "DNV T.2-3 B1", "DNV T.2-3 B2", "DNV T.2-3 C", "DNV T.2-3 C1", "DNV T.2-3 C2", "DNV T.2-3 D", "DNV T.2-3 E", "DNV T.2-3 F", "DNV T.2-3 F1", "DNV T.2-3 F3", "DNV T.2-3 G", "DNV T.2-3 W1", "DNV T.2-3 W2", "DNV T.2-3 W3", "DNV T.2-3 T", "EC3 FAT160", "EC3 FAT140", "EC3 FAT125", "EC3 FAT112", "EC3 FAT100", "EC3 FAT90", "EC3 FAT80", "EC3 FAT71", "EC3 FAT63", "EC3 FAT56", "EC3 FAT50", "EC3 FAT45", "EC3 FAT40", "EC3 FAT36", "EC3 FAT160 vari", "EC3 FAT140 vari", "EC3 FAT125 vari", "EC3 FAT112 vari", "EC3 FAT100 vari", "EC3 FAT90 vari", "EC3 FAT80 vari", "EC3 FAT71 vari", "EC3 FAT63 vari", "EC3 FAT50 vari", "EC3 FAT45 vari", "EC3 FAT40 vari", "EC3 FAT36 vari"],
                    "title": "The Fatclass Schema",
                    "description": "Specify the S-N curves from the list of available S-N curves. Use “User defined” to specify S-N curve properties manually",
                    "examples": [
                        "IIW FAT160 steel"
                    ]
                },
                "fat": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The Fat Schema",
                    "description": "Weld fatigue class. Stress range at n_fat cycles",
                    "examples": [
                        100
                    ]
                },
                "fat_fact": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The fat_fact Schema",
                    "description": "Scale factor for FAT value. E.g. to apply a thickness or temperature modification factor",
                    "examples": [
                        1.
                    ]
                },
                "n_fat": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The n_fat Schema",
                    "description": "Number of cycles for defining FAT. (IIW: Default = 2e6 cycles.)",
                    "examples": [
                        2000000
                    ]
                },
                "n_c": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The n_c Schema",
                    "description": "Break point between slope m_1 and m_2. (IIW: Default = 10e6 cycles.)",
                    "examples": [
                        10000000
                    ]
                },
                "m_1": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The M1 Schema",
                    "description": "S-N curve slope for N < n_c. (IIW: Default = 5 for Nominal)",
                    "examples": [
                        5
                    ]
                },
                "m_2": {
                    "type": "number",
                    "minimum": 0,
                    "title": "The M2 Schema",
                    "description": "S-N curve slope for N > n_c. (IIW: Default = 22)",
                    "examples": [
                        22
                    ]
                }
            },
            "oneOf": [
                {"title": "test",
                    "required": [
                        "class"
                    ]
                },
                {
                    "allOf": [
                        {
                            "required": [
                                "fat"
                            ]
                        },
                        {
                            "required": [
                                "n_fat"
                            ]
                        },
                        {
                            "required": [
                                "n_c"
                            ]
                        },
                        {
                            "required": [
                                "m_1"
                            ]
                        },
                        {
                            "required": [
                                "m_2"
                            ]
                        }
                    ]
                }
            ]

        },
        "mean_stress_theory": {
            "type": "object",
            "title": "The mean_stress_theory Schema",
            "description": "Specify mean stress theory",
            "properties": {
                "theory": {
                "type": "string",
                "enum": ["Goodman","Gerber","Soderberg"],
                "title": "The theory Schema",
                "description": "Specify mean stress theory",
                "examples": [
                    "Goodman"
                ]
                },
                "ultimate_limit": {
                "type": "number",
                "minimum": 0,
                "title": "The ultimate_limit Schema",
                "description": "Ultimate limit",
                "examples": [
                    500
                ]
                },
                "yield_limit": {
                "type": "number",
                "minimum": 0,
                "title": "The yield_limit Schema",
                "description": "Yield Limit",
                "examples": [
                    200
                ]
                }
                },
                "oneOf": [
                  {
                    "properties": {
                      "theory": {"enum": ["Goodman","Gerber"]}
                    },
                    "required": ["ultimate_limit"]
                  },
                  {
                    "properties": {
                      "theory": {"enum": ["Soderberg"]}
                    },
                    "required": ["yield_limit"]
                  }
                ]
        },
        "stress_unit": {
            "type": "string",
            "enum": ["pa","Pa","PA","mpa","Mpa","MPa","psi","Psi","PSI","ksi","Ksi","KSI"],
            "title": "The stress_unit Schema",
            "description": "Stress unit for the inputs",
            "examples": [
                "MPa"
            ]
        },
        "stress_data": {
            "type": "object",
            "title": "The stress_data Schema",
            "description": "Stress data inputs",
            "examples": [
                {
                    "bin1": {
                        "sa": 0.5,
                        "sm": 0.11,
                        "cycles": 0.38
                    }
                }
            ],
            "properties": {
                "/": {}
            },
            "patternProperties": {
                "^([0-9]+)+$": {
                    "type": "object",
                    "title": "The Bin1 Schema",
                    "properties": {
                        "sm": {
                            "type": "number",
                            "title": "The Sm Schema",
                            "description": "An explanation about the purpose of this instan_ce.",
                            "examples": [
                                0.11
                            ]
                        },
                        "sa": {
                            "type": "number",
                            "title": "The Sa Schema",
                            "description": "An explanation about the purpose of this instan_ce.",
                            "examples": [
                                0.5
                            ]
                        },
                        "cycles": {
                            "type": "number",
                            "title": "The Cycles Schema",
                            "description": "An explanation about the purpose of this instan_ce.",
                            "examples": [
                                0.38
                            ]
                        }},
                    "description": "An explanation about the purpose of this instan_ce.",
                    "examples": [
                        {
                            "sa": 0.11,
                            "cycles": 0.38,
                            "sm": 0.5
                        }
                    ],
                    "required": [
                        "sa",
                        "cycles"
                    ]
                    
                }
            },
          "additionalProperties": False
        },
        "serie_data": {
            "type": "object",
            "title": "The serie_data Schema",
            "description": "An explanation about the purpose of this instan_ce.",
            "examples": [
                {
                    "nbins": 3.0,
                    "series": [
                        0.4,
                        0.4220859399104398,
                        0.43617274661485916,
                    ],
                    "maxrange": 10.0
                }
            ],
            "additionalProperties": True,
            "required": [
                "series"
            ],
            "properties": {
                "series": {
                    "type": "array",
                    "title": "The Series Schema",
                    "description": "An explanation about the purpose of this instan_ce.",
                    "examples": [
                        [
                            0.4,
                            0.4220859399104398,
                            0.43617274661485916
                        ]
                    ],
                    "additionalItems": True,
                    "items": {
                        "type": "number",
                        "title": "The Items Schema",
                        "description": "An explanation about the purpose of this instan_ce.",
                        "examples": [
                            0.4,
                            0.4220859399104398,
                            0.43617274661485916
                        ]
                    }
                },
                "nbins": {
                    "type": "integer",
                    "title": "The Nbins Schema",
                    "description": "An explanation about the purpose of this instan_ce.",
                    "default": 0,
                    "examples": [
                        3.0
                    ]
                },
                "maxrange": {
                    "type": "number",
                    "title": "The Maxrange Schema",
                    "description": "An explanation about the purpose of this instan_ce.",
                    "default": 0,
                    "examples": [
                        10.0
                    ]
                }
            }
        }
        
    },
    "oneOf": [
        {
            "required": [
                "serie_data"
            ]
        },
        {
            "required": [
                "stress_data"
            ]
            
        }
    ]
}
    ,
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
