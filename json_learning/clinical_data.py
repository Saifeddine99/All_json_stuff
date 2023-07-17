import streamlit as st

from json_learning.clinical_condition import clinical_cond,previous_state,hba1c_records,other_analyses_records,current_medication,symptomatic,get_CVRFs

import json
import os

def all_hba1czz_not_null(hba1c_records_):
    for item in hba1c_records_:
        if(item==0):
            return(False)
    return(True)

def treatment_not_empty(current_drugs,previous_state_):
    if(bool(current_drugs)==False and previous_state_ !='First time'):
        return(False)
    else:
        return(True)

def clinical_data_():

    st.markdown("<h1 style='color: #0B5345;'>Clinical data:</h1>", unsafe_allow_html = True)
    st.write("#")

    # This function allows us to know whether it's patient's first time to get treatment or already getting
    previous_state_ = previous_state()

    hba1c_records_=hba1c_records(previous_state_)

    symptoms=symptomatic()
    current_drugs=current_medication(previous_state_)

    current_BMI,current_eGFR,current_UACR=other_analyses_records()
    CVRFs=get_CVRFs(current_BMI, current_eGFR,current_UACR)
    # Let's ask about the clinical condition :
    frailty,heart_failure,established_CVD,hepatic_steatosis,strokes=clinical_cond()

    full_path_clinical_data = os.path.join('json_learning', 'MyAnalytics.v3-composition.example.json')

    if(treatment_not_empty(current_drugs,previous_state_) and all_hba1czz_not_null(hba1c_records_) and (current_eGFR>0) and (current_UACR>0) and (current_BMI>0)):
        # Opening JSON files:

        #Clinical data file:
        with open(full_path_clinical_data, 'r') as openfile:
            # Reading from json file
            json_object_clincal_data = json.load(openfile)

        #Clinical conditions:
        json_object_clincal_data=add_clinical_data(json_object_clincal_data,frailty,heart_failure,established_CVD,hepatic_steatosis,strokes,symptoms,hba1c_records_,current_eGFR,current_UACR,current_drugs,current_BMI,CVRFs)

        # Serializing json
        json_object_clincal_data = json.dumps(json_object_clincal_data, indent=4)

        st.write("#")
        st.write("#")
        st.subheader("You can download the 'Clinical data' related to this patient from here:")
        st.write("#")

        col1, col2, col3 = st.columns([4,3,3])
        with col2:
            download_clinical = st.download_button('Download clinical data', json_object_clincal_data, file_name="clinical data.json")

        if (download_clinical):
            st.write("#")
            st.success(": File saved well " ,icon="✅")
    
    else:
        st.write("#")
        st.error(": One of the values you entered is invalid, Please check them carefully!",icon="⛔")


def add_clinical_data(json_object_clincal_data,frailty,heart_failure,established_CVD,hepatic_steatosis,strokes,symptoms,hba1c_records_,current_eGFR,current_UACR,current_drugs,current_BMI,CVRFs):
    if(frailty=="YES"):
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["symbol"]["value"]=frailty
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["value"]=1
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["symbol"]["defining_code"]["code_string"]="at0011"

    if(heart_failure=="YES"):    
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["value"]=heart_failure
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["value"]=1
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["defining_code"]["code_string"]="at0013"

    if(established_CVD=="YES"):    
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["value"]=established_CVD
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["value"]=1
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["defining_code"]["code_string"]="at0015"            

    if(hepatic_steatosis=="YES"):
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["value"]=hepatic_steatosis
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["value"]=1
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["defining_code"]["code_string"]="at0020"   
    
    if(strokes=="YES"):
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["symbol"]["value"]=strokes
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["value"]=1
        json_object_clincal_data["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["symbol"]["defining_code"]["code_string"]="at0023"   

    if(symptoms=="YES"):
        json_object_clincal_data["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["value"]=symptoms
        json_object_clincal_data["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["value"]=1
        json_object_clincal_data["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["defining_code"]["code_string"]="at0006"

    #Laboratory test results:
    for number,record in enumerate(hba1c_records_):
        if number==0:
            json_object_clincal_data["content"][2]["data"]["events"][number]["data"]["items"][0]["value"]["value"]="current HbA1c"
        elif number==1:
            json_object_clincal_data["content"][2]["data"]["events"][number]["data"]["items"][0]["value"]["value"]="previous HbA1c"
        elif number==2:
            json_object_clincal_data["content"][2]["data"]["events"][number]["data"]["items"][0]["value"]["value"]="before previous HbA1c"

        json_object_clincal_data["content"][2]["data"]["events"][number]["data"]["items"][1]["items"][0]["value"]["value"]=str(record)

    #current_eGFR:
    json_object_clincal_data["content"][2]["data"]["events"][3]["data"]["items"][0]["value"]["value"]="current_eGFR"
    json_object_clincal_data["content"][2]["data"]["events"][3]["data"]["items"][1]["items"][0]["value"]["value"]=str(current_eGFR)

    #current_UACR:
    json_object_clincal_data["content"][2]["data"]["events"][4]["data"]["items"][0]["value"]["value"]="current_UACR"
    json_object_clincal_data["content"][2]["data"]["events"][4]["data"]["items"][1]["items"][0]["value"]["value"]=str(current_UACR)

    #Medication:
    for number,key in enumerate(current_drugs.keys()):

        drug=key
        dose=current_drugs[key]

        if number<10:
            json_object_clincal_data["content"][3]["data"]["events"][number]["data"]["items"][0]["value"]["value"]=drug
            json_object_clincal_data["content"][3]["data"]["events"][number]["data"]["items"][1]["value"]["value"]=dose
        
    #Body Mass Index:
    json_object_clincal_data["content"][4]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"]=current_BMI

    #Cardiovascular factors:
    for number,cvrf in enumerate(CVRFs):
        if number<6:
            json_object_clincal_data["content"][5]["data"]["events"][number]["data"]["items"][0]["value"]["value"]=cvrf

    return(json_object_clincal_data)