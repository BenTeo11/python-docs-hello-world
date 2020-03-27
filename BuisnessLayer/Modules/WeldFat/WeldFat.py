from flask import Flask,jsonify, request, Response
import json
import uuid
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *

from .WeldFat_Pref import *
from math import *

def WeldFat(timestamp,_componentId, jsonInput): 
    """Iterate cycles in the series.

    Parameters
    ----------
    timestamp (datetime.datetime): 
    _componentId (string): "e9fafc85-5f4d-422e-8988-6545890f202c"
    jsonInput (string):  
        {
        "destinationModule": "WeldFat",
        "data": {
                "ultimateLimit": 400.0, 
                "Stress_Data": {
                    "1": [100, 5, 100000], 
                    "2": [200, 5, 100000000]
                    }, 
                "yieldLimit": 200.0, 
                "fatClass": ["IIW FAT125 steel",,,,,, ]
                 -> "fatClass": ["User Defined",fat,Nfat,Nc,m1,m2]
                    fat : stress range at Nfat cycles
                    Nfat : Number of cycles for defining fat
                    Nc : Break point between slope m1 and m2
                    m1 : S-N curve slope for N<Nc
                    m2 : S-N curve slope for N>Nc
                "meanStressTheory": "Goodman", 
                "Method": "nominalFatigue",
                "stressUnit": "MPa"
            }
        }
    Returns
    ------
    resDict dictionary as json
    
    resDict['Cumulative Damage [-]']
    resDict['Safety factor life [#blocks]']
    resDict['Equivalent Stress range']
    resDict['Safety factor stress [-]']
    resDict['rst'] : Fatigue result per bin as below
        resDict['rst'][bin]['Life [N]']
        resDict['rst'][bin]['log10(Life) [N]']
        resDict['rst'][bin]['Damage per block [-]']
        resDict['rst'][bin]['Safety factor life [#blocks]']
        
    """
    # read json inputs
    print(jsonInput)
    Input        = {} 
    Input        = json.loads(jsonInput)
    # Define unit conversion from user units to SI units
    stressUnit   = Input['stressUnit']
    SI           = {'mpa':1.0e6,'psi':6894.76,'ksi':6894757.29}
    convStressSI = SI[stressUnit.lower()]
    
    # get S-N Curve Nominal and Linearized Stress from preference file
    if Input['Method']=='nominalFatigue':
        fat     = fat_Nom[0]*SI[fat_Nom[1].lower()]
        fatFact = 1.
        Nfat    = Nfat_Nom
        Nc      = Nc_Nom
        m1      = m1_Nom
        m2      = m2_Nom
    else : 
        print ('error method')
    # get fatclass parameters
    fatClass = Input['fatClass'][0]
    if fatClass == 'User Defined':
        Nfat     = Input['fatClass'][1]
        fatFact  = Input['fatClass'][2]
        N0       = Input['fatClass'][3]
        m0       = Input['fatClass'][4]
        Ncutoff  = Input['fatClass'][5]
    else:
        N0       = fatClassDict[fatClass]['N0']
        m0       = fatClassDict[fatClass]['m0']
        Ncutoff  = fatClassDict[fatClass]['Ncutoff']
    #get mean stress theory parameter
    UTS = Input['ultimateLimit']*convStressSI
    SY  = Input['yieldLimit']*convStressSI
    if Input['meanStressTheory'] in ['Goodman','Gerber']:
        Rm = convStressSI*UTS
        Ry = 0.9*Rm
    elif Input['meanStressTheory'] == 'Soderberg': 
        Ry = convStressSI*SY
    elif Input['meanStressTheory'] == 'None': 
        if Input['Method'] in ['nominalFatigue', 'hotSpotFatigue']: 
            Ry = convStressSI*SY
        else: 
            Ry = 0.0

    # calculate result per bin
    resDict = {}
    resDict['Cumulative Damage [-]']        = 0.
    resDict['Safety factor life [#blocks]'] = 0.
    resDict['Equivalent Stress range']      = 0.
    resDict['Safety factor stress [-]']     = 0.
    resDict['rst']                          = {}
    
    for bin in Input['Stress_Data'].keys():
        # init result dictionary
        _rst_dic_per_bin                                 = {}
        _rst_dic_per_bin['Life [N]']                     = 0.0
        _rst_dic_per_bin['log10(Life) [N]']              = 0.0
        _rst_dic_per_bin['Damage per block [-]']         = 0.0
        _rst_dic_per_bin['Safety factor life [#blocks]'] = 0.0
        # intermediate parameters
        log10SN1 = log10(fat*fatFact)+(log10(Nfat)-log10(N0))/m1
        SN1      = 10**(log10SN1)
        SN0      = 10**(log10SN1+log10(N0)/m0)
        SNc      = 10**(log10(fat*fatFact)-(log10(Nc)-log10(Nfat))/m1)
        # calculate SNb
        cycles   = Input['Stress_Data'][bin][2]
        if cycles <= N0: 
            SNb = 10**(log10SN1+(log10(N0)-log10(cycles))/m0)
        elif cycles <= Nc: 
            SNb = 10**(log10(SNc)+(log10(Nc)-log10(cycles))/m1)
        else: 
            SNb = 10**(log10(SNc)-(log10(cycles)-log10(Nc))/m2)

        # mean stress theory
        warningUTS = False
        warningYield = False
        sm = Input['Stress_Data'][bin][0]*convStressSI
        sa = Input['Stress_Data'][bin][1]*convStressSI
        if Input['meanStressTheory'] == 'Goodman':
            if 0.0 < sm:
                sa /= 1-sa/Rm
            elif abs(sm)>= Rm:
                sa = 1.01*SN0
                warningUTS = True
        elif Input['meanStressTheory'] == 'Gerber':
            if abs(sm)<Rm:
                sa /= (1-sa)/Rm**2
            elif sm>= Rm:
                sa>=1.01*SN0
                warningUTS = True
        elif Input['meanStressTheory'] == 'Soderberg': 
            if 0.0 < sm < Ry: 
                sa /= (1-sa/Ry)
            elif abs(sm) >= Ry:
                sa = 1.01*SN0
                warningYield = True
        else:
            pass
            
        warningRangeNom = False
        warningRangeHS = False
        #warningStressMax = False
        if Input['Method'] =='nominalFatigue':
            if Input['Stress_Data'][bin][1]*convStressSI > 1.5*Ry: 
                warningRangeNom = True
                #if resDict['Stress max'][n] > Ry: warningStressMax = True
                #if resDict['Stress min'][n] < -Ry: warningStressMax = True
        elif Input['Method'] == 'hotSpotFatigue':
            if Input['Stress_Data'][bin][1]*convStressSI > 2.0*Ry: 
                warningRangeHS = True
                #if resDict['Stress max'][n] > Ry: warningStressMax = True
                #if resDict['Stress min'][n] < -Ry: warningStressMax = True
                
                
        # Calculate life and store result
        if sa > SN0:
            _rst_dic_per_bin['log10(Life) [N]']              = -1.0
            _rst_dic_per_bin['Life [N]']                     = 0.0
            _rst_dic_per_bin['Damage per block [-]']         = 100.0
            _rst_dic_per_bin['Safety factor life [#blocks]'] = 0.0
        elif sa> SN1:
            _rst_dic_per_bin['log10(Life) [N]']              = log10(N0) - m0*(log10(sa)-log10SN1)
            _rst_dic_per_bin['Life [N]']                     = 10**_rst_dic_per_bin['log10(Life) [N]']
        elif sa > SNc:
            _rst_dic_per_bin['log10(Life) [N]']              = log10(Nc) - m1*(log10(sa)-log10(SNc))
            _rst_dic_per_bin['Life [N]']                     = 10**_rst_dic_per_bin['log10(Life) [N]']
        elif sa > 0.0:
            _rst_dic_per_bin['log10(Life) [N]']              = min(log10(Ncutoff),log10(Nc) + m2*(log10(SNc) - log10(sa)))
            _rst_dic_per_bin['Life [N]']                     = 10**_rst_dic_per_bin['log10(Life) [N]']
        else:
            _rst_dic_per_bin['log10(Life) [N]']              = log10(Ncutoff)
            _rst_dic_per_bin['Life [N]']                     = Ncutoff
        if _rst_dic_per_bin['Life [N]']> 0: 
            _rst_dic_per_bin['Damage per block [-]']         = cycles/_rst_dic_per_bin['Life [N]']
            _rst_dic_per_bin['Safety factor life [#blocks]'] = 1/_rst_dic_per_bin['Damage per block [-]']
        _rst_dic_per_bin['Safety factor stress [-]']         = min(100.0,SNb/max(1,sa))
        # store results
        resDict['rst'][bin]=_rst_dic_per_bin

    #Cumulated Damage  

    cum_damage = 0.
    for bin in Input['Stress_Data'].keys():
        cum_damage += resDict['rst'][bin]['Damage per block [-]']
    resDict['Cumulative Damage [-]'] = cum_damage
    if cum_damage > 1e-5:
        resDict['Safety factor life [#blocks]'] = 1.0/cum_damage
        NSeqv                                   = cycles/cum_damage
    else:
        resDict['Safety factor life [#blocks]'] = 1e5
        NSeqv = Ncutoff

    if NSeqv <= N0: 
        Seqv                                    = 10**(log10SN1+(log10(N0)-log10(NSeqv))/m0)
    elif NSeqv <= Nc: 
        Seqv                                    = 10**(log10(SNc)+(log10(Nc)-log10(NSeqv))/m1)
    elif NSeqv < Ncutoff: 
        Seqv                                    = 10**(log10(SNc)-(log10(NSeqv)-log10(Nc))/m2)
    else: 
        Seqv                                    = SNb/100.0
    resDict['Equivalent Stress range']  = Seqv
    resDict['Safety factor stress [-]'] = min(100.0,SNb/Seqv)

    #insert the result to the 'Result' database
    data = formatTheResultForDB(resDict)
    #_resultTimeStamp = datetime.datetime.utcnow()
    Result.add_data(timestamp, datetime.datetime.utcnow() , _componentId, data)
