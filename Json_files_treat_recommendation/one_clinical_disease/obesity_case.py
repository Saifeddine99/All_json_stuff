from Json_files_treat_recommendation.target import target

def obese(hba1c_records,previous_state,current_BMI,med_dose_last_time):

    full_dose= "full dose"
    second_or_third_med_level=['DPP4i', 'SGLT2i', 'Pio', 'SU']

    next_date="Your next check is after 3 months"
    proposed_med={}
    if(previous_state=="First time"):
        proposed_med["Metformin"]=full_dose
    else:
        #The target variable represents the threshold to decide whether the patient achieved objective or not
        target_=6.5 ####target(previous_state,med_dose_last_time)
        proposed_med=med_dose_last_time
        current_hba1c=hba1c_records[0]
        if(current_hba1c>target_):
            if(["Metformin"] == list(med_dose_last_time.keys())):
                proposed_med["Metformin"]=full_dose
                if(current_BMI>35):
                    proposed_med["SGLT2i or GLP1RA; GLP-1RA is preferred here"]=full_dose
                    proposed_med["Consider also bariatric surgery"]="∅"
                else:
                    proposed_med["SGLT2i or GLP1RA"]=full_dose
                
            elif("Metformin" in med_dose_last_time and "SGLT2i" in med_dose_last_time and len(med_dose_last_time)==2):
                proposed_med["Metformin"]=full_dose
                proposed_med["SGLT2i"]=full_dose
                second_or_third_med_level.remove('SGLT2i')
                proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose
            elif("Metformin" in med_dose_last_time and "GLP1RA" in med_dose_last_time and len(med_dose_last_time)==2):
                proposed_med["Metformin"]=full_dose
                proposed_med["GLP1RA"]=full_dose
                second_or_third_med_level.remove('DPP4i')
                proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose
            elif("Metformin" in med_dose_last_time and not("Basal insulin" in med_dose_last_time) and len(med_dose_last_time)>=3 and (("SGLT2i" in med_dose_last_time and not("GLP1RA" in med_dose_last_time)) or ("GLP1RA" in med_dose_last_time and not("DPP4i" in med_dose_last_time)))):
                drugs=list(med_dose_last_time.keys())
                drugs.remove("Metformin")
                if("GLP1RA"in drugs):  
                    drugs.remove("GLP1RA")
                logic_drugs=1
                for item in drugs:
                    if(item not in second_or_third_med_level):
                        logic_drugs=0
                if(logic_drugs==1): 
                    proposed_med={}
                    proposed_med["Basal insulin"]=full_dose
                else:
                    proposed_med={}
                    proposed_med["Can't recommended treatment for this case !"]=""
            elif("Basal insulin" in med_dose_last_time):
                proposed_med={}
                proposed_med["Basal insulin"]= full_dose
            else:
                proposed_med={}
                proposed_med["Can't recommended treatment for this case !"]=""
        else:# Here we work on the case of patients who achieved the target
            next_date="Your next check is after 6 months"
            for med_item in med_dose_last_time.keys():
                proposed_med[med_item]=full_dose
    return(proposed_med,next_date)
