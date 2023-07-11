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


full_path = os.path.join('json_learning', 'MyAnalytics.v2-composition.example.json')

def all_hba1czz_not_null(hba1c_records_):
    for item in hba1c_records_:
        if(item==0):
            return(False)
    return(True)

def treatment_not_empty(current_drugs,previous_state_):
    if "clinical_data_button" not in st.session_state:
        st.session_state.clinical_data_button=False

    if "demographic_data_button" not in st.session_state:
        st.session_state.demographic_data_button=False

    if(bool(current_drugs)==False and previous_state_ !='First time'):
        return(False)
    else:
        return(True)

def patient_EHRs():
    #st.markdown("<h1 style='text-align: center; color: #17202A;'>This web app allows user to create 2 .json files one for demographics data and another for clinical data</h1>", unsafe_allow_html = True)
    st.write("#")

    name,surname,address,postal_code,birthday,dni,correct_dni,correct_postal_code=demongraphic_data()
    st.write("#")
    frailty,heart_failure,established_CVD,hepatic_steatosis,strokes,CVRFs,current_BMI,current_eGFR,current_UACR,current_drugs,symptoms,previous_state_,hba1c_records_,hba1c_string=clinical_data_()
    
    st.write("#")
    st.write("#")

    if( len(name)>0 and correct_postal_code and len(address)>0 and len(surname)>0 and correct_dni and treatment_not_empty(current_drugs,previous_state_) and all_hba1czz_not_null(hba1c_records_) and (current_eGFR>0) and (current_UACR>0) and (current_BMI>0) ):
        
        # Opening JSON file
        with open(full_path, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        
        json_object["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]=name
        json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["value"]=frailty
        json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["value"]=heart_failure
        json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["value"]=established_CVD
        json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["value"]=symptoms
        json_object["content"][2]["data"]["events"][1]["data"]["items"][1]["items"][1]["value"]["magnitude"]=str(current_UACR)
        json_object["content"][2]["data"]["events"][2]["data"]["items"][1]["items"][1]["value"]["magnitude"]=str(current_eGFR)
        json_object["content"][4]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"]=str(current_BMI)
        json_object["content"][3]["data"]["events"][0]["data"]["items"][0]["value"]["value"]=current_drugs
        json_object["content"][2]["data"]["events"][0]["data"]["items"][1]["items"][1]["value"]["magnitude"]=hba1c_string

        # Serializing json
        json_object = json.dumps(json_object, indent=4)
        col1, col2, col3 = st.columns([2,0.5,2])
        with col1:
            st.subheader("Clinical data related to this patient:")
            download_clinical = st.download_button('Download clinical data', json_object, file_name="clinical data of "+name+surname+".json",on_click=callback0)
            if (download_clinical or st.session_state.clinical_data_button):
                st.write("#")
                st.success(": File saved well " ,icon="✅")
        with col3:
            st.subheader("Dimographic data related to this patient:")
            download_demographics = st.download_button('Download demographic data', json_object, file_name="demographic data of "+name+surname+".json",on_click=callback1)
            if (download_demographics or st.session_state.demographic_data_button):
                st.write("#")
                st.success(": File saved well" ,icon="✅")
    else:
        st.error(": One of the values you entered is invalid, Please check them carefully!",icon="⛔")
