from json_learning.demographics import demongraphic_data
from json_learning.clinical_data import clinical_data_

import streamlit as st

import json
import os


def callback0():
    #Button was clicked!
    st.session_state.clinical_data_button= True

def callback1():
    #Button was clicked!
    st.session_state.demographic_data_button= True


full_path = os.path.join('json_learning', 'MyAnalytics.v3-composition.example.json')

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

def patient_EHRs():

    if "clinical_data_button" not in st.session_state:
        st.session_state.clinical_data_button=False

    if "demographic_data_button" not in st.session_state:
        st.session_state.demographic_data_button=False

    #st.markdown("<h1 style='text-align: center; color: #17202A;'>This web app allows user to create 2 .json files one for demographics data and another for clinical data</h1>", unsafe_allow_html = True)
    st.write("#")

    name,surname,address,postal_code,birthday,dni,correct_dni,correct_postal_code=demongraphic_data()
    st.write("#")
    frailty,heart_failure,established_CVD,hepatic_steatosis,strokes,CVRFs,current_BMI,current_eGFR,current_UACR,current_drugs,symptoms,previous_state_,hba1c_records_=clinical_data_()
    
    st.write("#")
    st.write("#")

    if( len(name)>0 and correct_postal_code and len(address)>0 and len(surname)>0 and correct_dni and treatment_not_empty(current_drugs,previous_state_) and all_hba1czz_not_null(hba1c_records_) and (current_eGFR>0) and (current_UACR>0) and (current_BMI>0) ):

        # Opening JSON file
        with open(full_path, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        
        #Clinical conditions:

        if(frailty=="YES"):
            json_object["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["symbol"]["value"]=frailty
            json_object["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["value"]=1
            json_object["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["symbol"]["defining_code"]["code_string"]="at0011"

        if(heart_failure=="YES"):    
            json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["value"]=heart_failure
            json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["value"]=1
            json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["defining_code"]["code_string"]="at0013"

        if(established_CVD=="YES"):    
            json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["value"]=established_CVD
            json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["value"]=1
            json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["defining_code"]["code_string"]="at0015"            

        if(hepatic_steatosis=="YES"):
            json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["value"]=hepatic_steatosis
            json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["value"]=1
            json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["defining_code"]["code_string"]="at0020"   
        
        if(strokes=="YES"):
            json_object["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["symbol"]["value"]=strokes
            json_object["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["value"]=1
            json_object["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["symbol"]["defining_code"]["code_string"]="at0023"   

        if(symptoms=="YES"):
            json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["value"]=symptoms
            json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["value"]=1
            json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["defining_code"]["code_string"]="at0006"

        #Laboratory test results:
        for number,record in enumerate(hba1c_records_):
            json_object["content"][2]["data"]["events"][number]["data"]["items"][0]["value"]["value"]="current HbA1c"
            json_object["content"][2]["data"]["events"][number]["data"]["items"][1]["items"][0]["value"]["value"]=str(record)

        #current_eGFR:
        json_object["content"][2]["data"]["events"][3]["data"]["items"][0]["value"]["value"]="current_eGFR"
        json_object["content"][2]["data"]["events"][3]["data"]["items"][1]["items"][0]["value"]["value"]=str(current_eGFR)

        #current_UACR:
        json_object["content"][2]["data"]["events"][4]["data"]["items"][0]["value"]["value"]="current_UACR"
        json_object["content"][2]["data"]["events"][4]["data"]["items"][1]["items"][0]["value"]["value"]=str(current_UACR)

        #Medication:
        for number,key in enumerate(current_drugs.keys()):

            drug=key
            dose=current_drugs[key]

            if number<10:
                json_object["content"][3]["data"]["events"][number]["data"]["items"][0]["value"]["value"]=drug
                json_object["content"][3]["data"]["events"][number]["data"]["items"][1]["value"]["value"]=dose
            
        #Body Mass Index:
        json_object["content"][4]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"]=current_BMI

        #Cardiovascular factors:
        for number,cvrf in enumerate(CVRFs):
            if number<6:
                json_object["content"][5]["data"]["events"][number]["data"]["items"][0]["value"]["value"]=cvrf



        # Serializing json
        json_object = json.dumps(json_object, indent=4)
        col1, col2, col3 = st.columns([2,0.5,2])
        with col1:
            st.subheader("Clinical data related to this patient:")
            download_clinical = st.download_button('Download clinical data', json_object, file_name="clinical data.json",on_click=callback0)
            if (download_clinical or st.session_state.clinical_data_button):
                st.write("#")
                st.success(": File saved well " ,icon="✅")
        with col3:
            st.subheader("Dimographic data related to this patient:")
            download_demographics = st.download_button('Download demographic data', json_object, file_name="demographic data.json",on_click=callback1)
            if (download_demographics or st.session_state.demographic_data_button):
                st.write("#")
                st.success(": File saved well" ,icon="✅")
    else:
        st.error(": One of the values you entered is invalid, Please check them carefully!",icon="⛔")
