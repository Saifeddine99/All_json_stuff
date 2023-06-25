def clinical_condition(obesity, elderly, frailty, chronic_kidney_disease, heart_failure, established_CVD,current_eGFR,current_UACR):

    if(obesity==elderly==frailty==chronic_kidney_disease==heart_failure==established_CVD=='NO'):
        return(['No other clinical conditions',])
    
    #Before deployment, this part needs to be checked by an expert:
    elif(chronic_kidney_disease=='YES' and current_eGFR<30):
        return(['critical_chronic_kidney_disease',])
    elif(established_CVD=='YES'):
        return(['established_cvd',])
    elif(frailty=='YES'):
        return(['age_or_frailty','frailty',])
    elif(heart_failure=='YES'):
        return(['heart_failure',])
    elif(chronic_kidney_disease=='YES'and ((30<=current_eGFR<=59) or (current_UACR>30))):
        return(['non_critical_chronic_kidney_disease',])
    elif(obesity=='YES'):
        return(['obesity',])
    elif(elderly=='YES'):
        return(['age_or_frailty','elderly',])
