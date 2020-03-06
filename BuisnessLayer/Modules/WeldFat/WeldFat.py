from flask import Flask,jsonify, request, Response
import json
import uuid
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *

from .WeldFat_Pref import *
from math import *

def WeldFat(timestamp,_componentId, jsonInput): 
    print (jsonInput)
    Input={} 
    Input=json.loads(jsonInput)
    '''Input['Method']='nominalFatigue'
    Input['fatClass']='IIW FAT125 steel'
    Input['Stress_Data']={}
    #Input['Stress_Data'][bin]=[av.,ampl.,cycles] 
    Input['Stress_Data'][1]=[10,5,10] #unit to be handle
    Input['Stress_Data'][2]=[20,5,10] #unit to be handle
    Input['meanStressTheory']='Goodman'
    Input['ultimateLimit']=500. #unit to be handle
    Input['yieldLimit']=200. #unit to be handle'''

    #get method parameter from preference file?
    if Input['Method']=='nominalFatigue':
        fat = fat_Nom
        fatFact = 1.
        Nfat = Nfat_Nom
        Nc = Nc_Nom
        m1 = m1_Nom
        m2 = m2_Nom
    else : 
        print ('error method')

    # get fatclass parameter
    fatClass = Input['fatClass']
    N0 = fatClassDict[fatClass]['N0']
    m0 = fatClassDict[fatClass]['m0']
    Ncutoff = fatClassDict[fatClass]['Ncutoff']

    #get mean stress theory parameter
    UTS=Input['ultimateLimit']
    SY=Input['yieldLimit']
    if Input['meanStressTheory']=='Goodman':
        Rm = UTS
        Ry = 0.9*Rm

    rst={}
    for bin in Input['Stress_Data'].keys():
        #initiate rst
        resDict = {}
        resDict['Life [N]']=0.0
        resDict['log10(Life) [N]']=0.0
        resDict['Damage per block [-]']=0.0
        resDict['Safety factor life [#blocks]']=0.0
        #resDict.Add('Safety factor stress [-]',0.0)
        #resDict.Add('Life quality [-]',1.0)

        #Calculate SNb
        log10SN1 = log10(fat[0]*fatFact)+(log10(Nfat)-log10(N0))/m1
        SN1 = 10**(log10SN1)
        SN0 = 10**(log10SN1+log10(N0)/m0)
        SNc = 10**(log10(fat[0]*fatFact)-(log10(Nc)-log10(Nfat))/m1)
        
        cycles = Input['Stress_Data'][bin][2]
        if cycles <= N0: 
                SNb = 10**(log10SN1+(log10(N0)-log10(cycles))/m0)
        elif cycles <= Nc: 
                SNb = 10**(log10(SNc)+(log10(Nc)-log10(cycles))/m1)
        else: 
                SNb = 10**(log10(SNc)-(log10(cycles)-log10(Nc))/m2)
        #Mean Stress th. => Sa 
        sm=Input['Stress_Data'][bin][0]
        sa=Input['Stress_Data'][bin][1]
        if Input['meanStressTheory'] == 'Goodman':
            if 0.0 < sm:
                sa/=1-sa/Rm
            elif abs(sm)>= Rm:
                sa = 1.01*SN0
        elif Input['meanStressTheory'] == 'Gerber':
            if abs(sm)<Rm:
                sa /= (1-sa)/Rm**2
            elif sm>= Rm:
                sa>=1.01*SN0
        elif Input['meanStressTheory'] == 'Soderberg': 
            if 0.0 < sm < Ry: 
                sa /= (1-sa/Ry)
            elif abs(sm) >= Ry:
                sa = 1.01*SN0
        else:
            pass

        #Calculate life
        if sa > SN0:
            resDict['log10(Life) [N]'] = -1.0
            resDict['Life [N]'] = 0.0
            resDict['Damage per block [-]']= 100.0
            resDict['Safety factor life [#blocks]']= 0.0
        elif sa> SN1:
            resDict['log10(Life) [N]'] = log10(N0) - m0*(log10(sa)-log10SN1)
            resDict['Life [N]']= 10**resDict['log10(Life) [N]']
        elif sa > SNc:
            resDict['log10(Life) [N]'] = log10(Nc) - m1*(log10(sa)-log10(SNc))
            resDict['Life [N]']= 10**resDict['log10(Life) [N]']
        elif sa > 0.0:
            resDict['log10(Life) [N]'] = min(log10(Ncutoff),log10(Nc) + m2*(log10(SNc) - log10(sa)))
            resDict['Life [N]'] = 10**resDict['log10(Life) [N]']
        else:
            resDict['log10(Life) [N]'] = log10(Ncutoff)
            resDict['Life [N]'] = Ncutoff
        if resDict['Life [N]']> 0: 
            resDict['Damage per block [-]'] = cycles/resDict['Life [N]']
            resDict['Safety factor life [#blocks]'] = 1/resDict['Damage per block [-]']
        resDict['Safety factor stress [-]'] = min(100.0,SNb/max(1,sa))
        
        rst[bin]=resDict

    #Cumulated Damage  
    resDict = {}
    resDict['Cumulative Damage [-]']=0.
    resDict['Safety factor life [#blocks]']=0.
    resDict['Equivalent Stress range']=0.
    resDict['Safety factor stress [-]']=0.
    resDict['rst']={}
    cum_damage = 0.

    for bin in Input['Stress_Data'].keys():
        cum_damage += rst[bin]['Damage per block [-]']
    resDict['Cumulative Damage [-]']=cum_damage
    if cum_damage > 1e-5:
        resDict['Safety factor life [#blocks]'] = 1.0/cum_damage
        NSeqv = cycles/cum_damage
    else:
        resDict['Safety factor life [#blocks]'] = 1e5
        NSeqv = Ncutoff

    if NSeqv <= N0: 
        Seqv = 10**(log10SN1+(log10(N0)-log10(NSeqv))/m0)
    elif NSeqv <= Nc: 
        Seqv = 10**(log10(SNc)+(log10(Nc)-log10(NSeqv))/m1)
    elif NSeqv < Ncutoff: 
        Seqv = 10**(log10(SNc)-(log10(NSeqv)-log10(Nc))/m2)
    else: 
        Seqv = SNb/100.0
    resDict['Equivalent Stress range']= Seqv
    resDict['Safety factor stress [-]']= min(100.0,SNb/Seqv)
    resDict['rst']=rst
    print (resDict)
    #print (rst)
    #insert the result to the 'Result' database
    data = formatTheResultForDB(resDict)

    #_resultTimeStamp = datetime.datetime.utcnow()
    Result.add_data(timestamp, datetime.datetime.utcnow() , _componentId, data)
