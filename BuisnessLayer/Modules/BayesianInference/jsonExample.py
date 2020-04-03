#Expected input format

input = {
	"BinValueDistribution": {
		"PriorTable": {
			"stress": {
				"kind": "normal",
				"mean": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
				"sd": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
			},
			"temp": {
				"kind": "normal",
				"mean": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
				"sd": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
			},
			"labelX": {
				"kind": "normal",
				"mean": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
				"sd": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
			}

		}

	},
	"EvidenceBatch": {
		"StartTime": 1,
		"EndTime": 1,
		"LoadTable": {
			"stress": {
				"kind": "normal",
				"Entity": "BinDistribution",
				"Magnitude": [15, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
			},
			"temp": {
				"kind": "normal",
				"Entity": "BinDistribution",
				"Magnitude": [15, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
			},
			"labelX": {
				"kind": "studentt",
				"nu": 10,
				"Entity": "Bin distribution",
				"Magnitude": [15, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
			}

		}
	}
}