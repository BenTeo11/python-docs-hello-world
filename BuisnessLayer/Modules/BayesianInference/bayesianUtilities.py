import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Component ID
componentId = 'E54F8E4EE151417DB22DB80EB58042B1'


#Prior generators
def generateNormalPriors(input, key): 
    normalPriors = []
    for priorNum in range(len(input["BinValueDistribution"]["PriorTable"][key]["mean"])):
        normalPriors.append(pm.Normal("mu_" + key + "_" + str(priorNum), mu=input["BinValueDistribution"]["PriorTable"][key]["mean"][priorNum], sd=input["BinValueDistribution"]["PriorTable"][key]["sd"][priorNum]))
    return normalPriors

def generateLogNormalPriors(input, key):
    logNormalPriors = []
    for priorNum in range(len(input["BinValueDistribution"]["PriorTable"][key]["mean"])):
        logNormalPriors.append(pm.Lognormal("mu_" + key + "_" + str(priorNum), mu=input["BinValueDistribution"]["PriorTable"][key]["mean"][priorNum], sd=input["BinValueDistribution"]["PriorTable"][key]["sd"][priorNum]))
    return logNormalPriors

def generateUniformPriors(input, key):
    uniformPriors = []
    for priorNum in range(len(input["BinValueDistribution"]["PriorTable"][key]["low"])):
        uniformPriors.append(pm.Uniform("mu_" + key + "_" + str(priorNum), lower=input["BinValueDistribution"]["PriorTable"][key]["low"][priorNum], upper=input["BinValueDistribution"]["PriorTable"][key]["high"][priorNum]))
    return uniformPriors


#Likelihood generators
def generateNormalLikelihood(priors, input, key):
    normalLikelihoods = []
    for variableNum in range(len(priors)):
        normalLikelihoods.append(pm.Normal("ev_"+ key + "_" + str(variableNum), mu=priors[variableNum], observed=input["EvidenceBatch"]["LoadTable"][key]["Magnitude"][variableNum])) 
    return normalLikelihoods

def generateLogNormalLikelihood(priors, input, key):
    logNormalLikelihoods = []
    for variableNum in range(len(priors)):
        logNormalLikelihoods.append(pm.Lognormal("ev_"+ key + "_" + str(variableNum), mu=priors[variableNum], observed=input["EvidenceBatch"]["LoadTable"][key]["Magnitude"][variableNum])) #input["BinValueDistribution"]["PriorTable.1D"]["sd"][variableNum]
    
    return

def generateStudentTLikelihood(priors, input, key):
    studentTLikelihoods = []
    for variableNum in range(len(priors)):
        studentTLikelihoods.append(pm.StudentT("ev_"+ key + "_" + str(variableNum), nu=input["EvidenceBatch"]["LoadTable"][key]["nu"], mu=priors[variableNum], observed=input["EvidenceBatch"]["LoadTable"][key]["Magnitude"][variableNum])) #input["BinValueDistribution"]["PriorTable.1D"]["sd"][variableNum]
    return studentTLikelihoods


#Help functions
def printPosteriorInfo(HPD, trace):
    try: 
        print(pm.summary(trace, credible_interval=HPD).round(2))
    except:
        print("No summary available. Check function-input or perform sampling")
    return

def printPosteriorMeans(HPD, trace):
    try:
        print(pm.summary(trace, credible_interval=HPD).round(2)["mean"])
    except: 
        print("No summary available. Check function-input or perform sampling")
    return

def printPosteriorStd(summary, label, bin):
    try:
        print(pm.summary(trace, credible_interval=HPD).round(2)["sd"])
    except: 
        print("No summary available. Check function-input or perform sampling")
    return

def getPosteriorDataframe(HPD, trace):
    try: 
        result = pm.summary(trace, credible_interval=HPD).round(2)
    except: 
        print("No summary available. Check function-input or perform sampling")
    return result

def getPosteriorMeans(HPD, trace):
    try:
        result = pm.summary(trace, credible_interval=HPD).round(2)["mean"]
    except: 
        print("No summary available. Check function-input or perform sampling")
    return result

def getPosteriorSd(HPD, trace):
    try:
        result = pm.summary(trace, credible_interval=HPD).round(2)["sd"]
    except: 
        print("No summary available. Check function-input or perform sampling")
    return result




def RUL():
    #different for gears, welds? ++
    return

def accumulatedDamage(cycles, Fat, bins):
    #distribution of number of cycles at each load level. Miners rule? more advanced?
    return

def evaluateCorelation(label1, label2):
        #switchpoint analysis?
    return


