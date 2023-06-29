def medications(drugs_string):
    med_dict={}
    if(len(drugs_string)>0):
        drugs_list=drugs_string.split('/')
        for drug in drugs_list:
            drug_name,dose=drug.split(':')
            med_dict[drug_name]=dose
    return(med_dict)

def hba1c_records_list(hba1c):
    records_list=hba1c.split('/')
    hba1c_list=[]
    for record in records_list:
        hba1c_list.append(float(record))
    return(hba1c_list)

def extract_data(json_object): 

    name=json_object["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]
    age=int(json_object["content"][0]["data"]["events"][0]["data"]["items"][1]["value"]["value"])
    frailty=json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["value"]
    heart_failure=json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["value"]
    established_cvd=json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["value"]
    symptoms=json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["value"]
    current_UACR=float(json_object["content"][2]["data"]["events"][1]["data"]["items"][1]["items"][1]["value"]["magnitude"])   
    current_eGFR=float(json_object["content"][2]["data"]["events"][2]["data"]["items"][1]["items"][1]["value"]["magnitude"])
    current_BMI=float(json_object["content"][4]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"])   
    hba1c_records=hba1c_records_list(json_object["content"][2]["data"]["events"][0]["data"]["items"][1]["items"][1]["value"]["magnitude"])

    medication_dict=medications(json_object["content"][3]["data"]["events"][0]["data"]["items"][0]["value"]["value"])

    return(name,age,frailty,heart_failure,established_cvd,symptoms,current_UACR,current_eGFR,current_BMI,medication_dict,hba1c_records)
