#import numpy as np
#import matplotlib.pyplot as plt
import pymc3 as pm
import json
from BuisnessLayer.Modules.BayesianInference.bayesianUtilities import *
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *
import ast


priorGenerators = {"normal": generateNormalPriors, "lognormal": generateLogNormalPriors, "uniform": generateUniformPriors}
likelihoodGenerators = {"normal": generateNormalLikelihood, "lognormal": generateLogNormalLikelihood, "studentt": generateStudentTLikelihood}


def BayesianInference(timeStamp, userInfo, input):
    n_samples = 2000
    input = ast.literal_eval(input)
    result = {}
    for key in input["BinValueDistribution"]["PriorTable"].keys():
        with pm.Model() as model:
            priors = priorGenerators[input["BinValueDistribution"]["PriorTable"][key]["kind"]](input, key)
            likelihoodGenerators[input["EvidenceBatch"]["LoadTable"][key]["kind"]](priors, input, key)

            trace = pm.sample(n_samples, chains=4)
            
            ppc = pm.sample_posterior_predictive(trace)
            summary = pm.summary(ppc)
            summary = summary.to_dict()
            summary = dict(list(summary.items())[0: 4])
            result[str(key)] = summary
                
    result = formatTheResultForDB(result)
    Result.add_data(timeStamp, datetime.datetime.utcnow(), userInfo, result)
            
    return
