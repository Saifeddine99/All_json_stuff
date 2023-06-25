medium_dose="medium dose"
full_dose= "full dose"

#This function finds the name of the "ONE" chosen medication from the list.
def find_item_1(med_dose_last_time):
    item=''
    for key in med_dose_last_time:
        if (key != "nonpharmacological therapy" and key != "Metformin"):
            item=key
    return(item)

def recommended_treatment(med_dose_last_time,current_hba1c,target,current_symptoms_situation):

    #this is the list of the second/third level medications
    second_or_third_med_level=['DPP4i', 'SGLT2i', 'oral GLP1ra', 'Pio', 'SU']

    proposed_med=med_dose_last_time
    
#Here we are working on the case of a user using only nonpharmacological therapy
    if (("nonpharmacological therapy" in med_dose_last_time) and len(med_dose_last_time)==1):
        proposed_med["Metformin"]=medium_dose

    #Here we'll be working on the case of someone using only metformin
    elif ((("nonpharmacological therapy" in med_dose_last_time) and ("Metformin" in med_dose_last_time) and len(med_dose_last_time)==2) or (("Metformin" in med_dose_last_time) and len(med_dose_last_time)==1)):
        #proposed_med=med_dose_last_time
        if(med_dose_last_time["Metformin"] == medium_dose):
            if(target<current_hba1c<=8):
                proposed_med["Metformin"]=full_dose
            elif (8<current_hba1c<=9):
                proposed_med["Metformin"]=full_dose
                proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=medium_dose
            else:
                proposed_med={}
                proposed_med["Visit a doctor"]="Critical situation"
        else:
            proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=medium_dose
    # Here we're working on Metformin + only one drug from the list
    elif ((len(med_dose_last_time)==2 and not("nonpharmacological therapy" in med_dose_last_time) and not("Basal insulin" in med_dose_last_time) and ("Metformin" in med_dose_last_time)) or (("nonpharmacological therapy" in med_dose_last_time) and not("Basal insulin" in med_dose_last_time) and len(med_dose_last_time)==3 and ("Metformin" in med_dose_last_time))):
        symptoms="NO"
        if(current_hba1c>9):
                symptoms=current_symptoms_situation
        if(symptoms=="YES"):
            proposed_med={} 
            proposed_med["Metformin"]=full_dose
            proposed_med["Basal insulin"]=full_dose
        else:    
            first_med_from_list= find_item_1(med_dose_last_time)
            if(target<current_hba1c<=8):
                if(med_dose_last_time["Metformin"]==med_dose_last_time[first_med_from_list]==full_dose):
                    second_or_third_med_level.remove(first_med_from_list)
                    proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose
                else:
                    proposed_med["Metformin"]=full_dose
                    proposed_med[first_med_from_list]=full_dose    
            elif (8<current_hba1c<=9):
                proposed_med["Metformin"]=full_dose
                proposed_med[first_med_from_list]=full_dose 
                second_or_third_med_level.remove(first_med_from_list)
                proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose
            else:
                proposed_med={}
                proposed_med["Visit a doctor"]="Critical situation"
    # Here we're working on Metformin + strictly more than 1 drug from the list
    elif ((len(med_dose_last_time)>=3 and not("nonpharmacological therapy" in med_dose_last_time) and not("Basal insulin" in med_dose_last_time) and ("Metformin" in med_dose_last_time)) or (("nonpharmacological therapy" in med_dose_last_time) and not("Basal insulin" in med_dose_last_time) and len(med_dose_last_time)>=4 and ("Metformin" in med_dose_last_time))):
    
        if(target<current_hba1c<=8):
                #Here we will add another drug
                for key in med_dose_last_time:
                    if(key!= "nonpharmacological therapy"):
                        proposed_med[key]=full_dose
                    if(key != "nonpharmacological therapy" and key != "Metformin"):
                        second_or_third_med_level.remove(key)
                if( len(second_or_third_med_level)>0):
                    proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose  
                else:
                    proposed_med={}
                    proposed_med["Basal insulin"]=full_dose
        elif (8<current_hba1c<=9):
            proposed_med={}
            proposed_med["Basal insulin"]=full_dose
        else:
            proposed_med={}
            proposed_med["Visit a doctor"]="Critical situation"
    #Here we will work on the case of patient using met+ insulin
    elif (("Basal insulin" in med_dose_last_time) and ("Metformin" in med_dose_last_time) and (len(med_dose_last_time)==2)):
        proposed_med={}
        proposed_med["Metformin"]=full_dose
        symptoms="YES"
        if(current_hba1c<=9):
            symptoms=current_symptoms_situation
        if(symptoms=="NO"):
            proposed_med["You can choose any item from this list: {}".format(second_or_third_med_level)]=full_dose        
        else:
            proposed_med["Basal insulin"]=full_dose
    elif("Basal insulin" in med_dose_last_time):
        proposed_med={}
        proposed_med["Basal insulin"]= full_dose
    else:
        proposed_med={"this_cond":"Doesn't exist"}
    return(proposed_med)
