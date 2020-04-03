import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import json
from BuisnessLayer.Modules.bjornTesting.bayesianUtilities import *
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *
import ast

#The below function will be replaced by pm-prophet
def getBayesianCone(timeSeries, stepsToPredict, timeSeriesSamplingDist=pm.Normal, priorMean=0, priorMeanDist=None, priorSd=None, priorSdDist=pm.HalfNormal, numChains=1, n_samples=200):
    df = pd.DataFrame({"y": timeSeries})
    df = df.reindex(np.arange(len(timeSeries)+stepsToPredict))
    print(df)
    sd = priorSdDist("sd", priorSd)
    if priorMeanDist:
        mu = priorMeanDist("mu", mu=priorMean, sd=sd)
    else:
        mu=priorMean
    prior = pm.GaussianRandomWalk("prior", mu=mu, sd=sd, shape=len(df))
    trace = pm.sample(chains=numChains)
    pm.traceplot(trace)
    plt.show()
    return 