from flask import Flask,jsonify, request, Response
import json
import uuid
import datetime
from DatabaseLayer.DataModel import *
from BuisnessLayer.Utilities.HelpFunctions import *
from collections import deque, defaultdict
import rainflow
from .WeldFat_Pref import *
from math import *

def WeldFat(timestamp,_componentId, json_input): 

    """Iterate cycles in the series.

    Parameters
    ----------
    timestamp (datetime.datetime): 
    _componentId (string): "e9fafc85-5f4d-422e-8988-6545890f202c"
    jsonjson_obj (string):  
    Returns
    ------
    res_dict dictionary as json
    
    res_dict['cumulative_damage']
    res_dict['safety_factor_life_per_bin']
    res_dict['equivalent_stress_range']
    res_dict['safety_factor_stress']
    res_dict['rst'] : Fatigue result per bin as below
        res_dict['rst'][bin]['life']
        res_dict['rst'][bin]['log10_life']
        res_dict['rst'][bin]['damage_per_bin']
        res_dict['rst'][bin]['safety_factor_life_per_bin']
        
    """
    # read json json_objs
    json_obj        = {} 
    json_obj        = json.loads(json_input)
    # Define unit conversion from user units to stress_unit_dict units
    stress_unit   = json_obj['stress_unit']
    stress_unit_dict           = {'mpa':1.0e6,'psi':6894.76,'ksi':6894757.29}
    conv_stress = stress_unit_dict[stress_unit.lower()]
    # Get S-N Curve definition parameters
    if "class" not in json_obj["fatigue_class"]:
        fat_class = "User defined"
        fat     = json_obj["fatigue_class"]["fat"]*conv_stress
        n_fat    = json_obj["fatigue_class"]["n_fat"]
        n_c      = json_obj["fatigue_class"]["n_c"]
        m_1      = json_obj["fatigue_class"]["m_1"]
        m_2      = json_obj["fatigue_class"]["m_2"]
    else:
        fat_class = json_obj["fatigue_class"]["class"]
        fat     = fatClassDict[fat_class]['FAT'][0]*stress_unit_dict[fatClassDict[fat_class]['FAT'][1].lower()]
        n_fat    = fatClassDict[fat_class]['Nfat']
        n_c      = fatClassDict[fat_class]['Nc']
        m_1      = fatClassDict[fat_class]['m1']
        m_2      = fatClassDict[fat_class]['m2']
        
    if "fat_fact" not in json_obj["fatigue_class"]:
        fat_fact = 1.
    else:
        fat_fact = json_obj["fatigue_class"]["fat_fact"]
        
    if 'N0' in fatClassDict[fat_class]:
        n_0      = fatClassDict[fat_class]['N0']
    else:
        n_0 = 1
        
    if 'm0' in fatClassDict[fat_class]:
        m_0      = fatClassDict[fat_class]['m0']
    else:
        m_0 = 1
        
    if 'Ncutoff' in fatClassDict[fat_class]:
        n_cutoff = fatClassDict[fat_class]['Ncutoff']
    else:
        n_cutoff = 1
    # intermediate parameters
    log10_sn_1 = log10(fat*fat_fact)+(log10(n_fat)-log10(n_0))/m_1
    sn_1      = 10**(log10_sn_1)
    sn_0      = 10**(log10_sn_1+log10(n_0)/m_0)
    sn_c      = 10**(log10(fat*fat_fact)-(log10(n_c)-log10(n_fat))/m_1)
    # Get mean stress theory parameter
    if "mean_stress_theory" in json_obj:
        mean_stress_theory=json_obj['mean_stress_theory']['theory']  
        if mean_stress_theory in ['Goodman','Gerber']:
            UTS = json_obj['mean_stress_theory']['ultimate_limit']*conv_stress
            r_m = conv_stress*UTS
            r_y = 0.9*r_m
        elif mean_stress_theory == 'Soderberg': 
            SY  = json_obj['mean_stress_theory']['yield_limit']*conv_stress
            r_y = conv_stress*SY
        #elif json_obj['mean_stress_theory'] == 'None': 
        #    if json_obj['Method'] in ['nominalFatigue', 'hotSpotFatigue']: 
        #        r_y = conv_stress*SY
        #    else: 
        #        r_y = 0.0

    # Calculate result per bin
    res_dict = {}
    res_dict['cumulative_damage']        = 0.
    res_dict['safety_factor_life_per_bin'] = 0.
    res_dict['equivalent_stress_range']      = 0.
    res_dict['safety_factor_stress']     = 0.
    res_dict['rst']                          = {}
    
    if 'stress_data' not in json_obj.keys() and 'serie_data' in json_obj.keys():
        series=json_obj['serie_data']["series"]
        if 'nbins' in json_obj['serie_data'].keys(): 
            nbins = json_obj['serie_data']['nbins']
            max_range = max(series) - min(series)
            if 'maxrange' in json_obj['serie_data']:
                my_max_range =json_obj['serie_data']['maxrange']
                max_range = my_max_range
                if max_range < my_max_range:#add error message?
                    pass
                else:
                    print ("serie max range larger than given max range") 
            binsize = max_range / nbins
            counts_ix = defaultdict(int)
            for i in range(nbins):
                counts_ix[i] = 0
            # Apply mean stress theory before assigning to bin
            for low, high, mult in rainflow.extract_cycles(series):
                bin_index = int(abs(high - low) / binsize)
                sm=0.5 * (high + low)
                sa=high - low
                if "mean_stress_theory" in json_obj: #does not handle sn_0
                    sa=apply_mean_stress_theory(mean_stress_theory,sm,sa,sn_0,r_m,r_y)
                bin_index = int(abs(sa) / binsize)
                # handle possibility of range equaliing max range
                if bin_index == nbins:
                    bin_index = nbins - 1
                counts_ix[bin_index] += mult
            # save count data to dictionary where key is the range
            counts = dict(((k+1)*binsize,v) for k,v in counts_ix.items())
            cycles_list=sorted(counts.items())
            #print (cycles_list)
            json_obj['stress_data']={}
            for i in range(len(cycles_list)):
                json_obj['stress_data'][i]={'sa':cycles_list[i][0],'cycles':cycles_list[i][1],'sm':0.}
            if "mean_stress_theory" in json_obj:
                del json_obj["mean_stress_theory"]
        else:
            json_obj['stress_data']={}
            for i,(low, high, mult) in enumerate(rainflow.extract_cycles(series)):
                mean=0.5 * (high + low)
                rng=high - low
                json_obj['stress_data'][i]={'sa':rng,'cycles':mult,'sm':mean}
                
    #print(json_obj['stress_data'])

    for bin in json_obj['stress_data'].keys():
        cycles   = json_obj['stress_data'][bin]["cycles"]
        if cycles !=0.:
            # init result dictionary
            _rst_dic_per_bin                                 = {}
            _rst_dic_per_bin['life']                     = 0.0
            _rst_dic_per_bin['log10_life']              = 0.0
            _rst_dic_per_bin['damage_per_bin']         = 0.0
            _rst_dic_per_bin['safety_factor_life_per_bin'] = 0.0
            # calculate s_nb
            if cycles <= n_0: 
                s_nb = 10**(log10_sn_1+(log10(n_0)-log10(cycles))/m_0)
            elif cycles <= n_c: 
                s_nb = 10**(log10(sn_c)+(log10(n_c)-log10(cycles))/m_1)
            else: 
                s_nb = 10**(log10(sn_c)-(log10(cycles)-log10(n_c))/m_2)

            # mean stress theory
            sa = json_obj['stress_data'][bin]["sa"]*conv_stress
            if "mean_stress_theory" in json_obj and "sm" in json_obj['stress_data'][bin]:
                mean_stress_theory=json_obj['mean_stress_theory']['theory']
                sm = json_obj['stress_data'][bin]["sm"]*conv_stress
                sa=apply_mean_stress_theory(mean_stress_theory,sm,sa,sn_0,r_m,r_y)

        # Calculate life and store result
        if sa > sn_0:
            _rst_dic_per_bin['log10_life']              = -1.0
            _rst_dic_per_bin['life']                     = 0.0
            _rst_dic_per_bin['damage_per_bin']         = 100.0
            _rst_dic_per_bin['safety_factor_life_per_bin'] = 0.0
        elif sa> sn_1:
            _rst_dic_per_bin['log10_life']              = log10(n_0) - m_0*(log10(sa)-log10_sn_1)
            _rst_dic_per_bin['life']                     = 10**_rst_dic_per_bin['log10_life']
        elif sa > sn_c:
            _rst_dic_per_bin['log10_life']              = log10(n_c) - m_1*(log10(sa)-log10(sn_c))
            _rst_dic_per_bin['life']                     = 10**_rst_dic_per_bin['log10_life']
        elif sa > 0.0:
            _rst_dic_per_bin['log10_life']              = min(log10(n_cutoff),log10(n_c) + m_2*(log10(sn_c) - log10(sa)))
            _rst_dic_per_bin['life']                     = 10**_rst_dic_per_bin['log10_life']
        else:
            _rst_dic_per_bin['log10_life']              = log10(n_cutoff)
            _rst_dic_per_bin['life']                     = n_cutoff
        if _rst_dic_per_bin['life']> 0: 
            _rst_dic_per_bin['damage_per_bin']         = cycles/_rst_dic_per_bin['life']
            if _rst_dic_per_bin['damage_per_bin']!=0.:
                _rst_dic_per_bin['safety_factor_life_per_bin'] = 1/_rst_dic_per_bin['damage_per_bin']
            else:
                _rst_dic_per_bin['safety_factor_life_per_bin'] = 1.
        _rst_dic_per_bin['safety_factor_stress']         = min(100.0,s_nb/max(1,sa))
        # store results
        res_dict['rst'][bin]=_rst_dic_per_bin

    #Cumulated Damage  
    cum_damage = 0.
    for bin in json_obj['stress_data'].keys():
        cum_damage += res_dict['rst'][bin]['damage_per_bin']
    res_dict['cumulative_damage'] = cum_damage
    if cum_damage > 1e-5:
        res_dict['safety_factor_life_per_bin'] = 1.0/cum_damage
        n_seqv                                   = cycles/cum_damage
    else:
        res_dict['safety_factor_life_per_bin'] = 1e5
        n_seqv = n_cutoff

    if n_seqv <= n_0: 
        s_eqv                                    = 10**(log10_sn_1+(log10(n_0)-log10(n_seqv))/m_0)
    elif n_seqv <= n_c: 
        s_eqv                                    = 10**(log10(sn_c)+(log10(n_c)-log10(n_seqv))/m_1)
    elif n_seqv < n_cutoff: 
        s_eqv                                    = 10**(log10(sn_c)-(log10(n_seqv)-log10(n_c))/m_2)
    else: 
        s_eqv                                    = s_nb/100.0
    res_dict['equivalent_stress_range']  = s_eqv
    res_dict['safety_factor_stress'] = min(100.0,s_nb/s_eqv)
    #insert the result to the 'Result' database
    data = formatTheResultForDB(res_dict)
    #_resultTimeStamp = datetime.datetime.utcnow()
    Result.add_data(timestamp, datetime.datetime.utcnow() , _componentId, data)


def apply_mean_stress_theory(mean_stress_theory,sm,sa,sn_0,r_m,r_y):
    if mean_stress_theory == 'Goodman':
            if 0.0 < sm:
                sa /= 1-sa/r_m
            elif abs(sm)>= r_m:
                sa = 1.01*sn_0 
    elif mean_stress_theory == 'Gerber':
            if abs(sm)<r_m:
                sa /= (1-sa)/r_m**2
            elif sm>= r_m:
                sa>=1.01*sn_0
    elif mean_stress_theory == 'Soderberg': 
            if 0.0 < sm < r_y: 
                sa /= (1-sa/r_y)
            elif abs(sm) >= r_y:
                sa = 1.01*sn_0
    else:
            pass
    return sa