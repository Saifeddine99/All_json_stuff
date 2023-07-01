import streamlit as st
import json
import os

full_path = os.path.join('json_learning', 'MyAnalytics.v2-composition.example.json')

from json_learning.clinical_condition import clinical_cond,previous_state,hba1c_records,other_analyses_records,current_medication,symptomatic,get_CVRFs

def all_hba1czz_are_floats(hba1c_records_):
    for item in hba1c_records_:
        if(not (isinstance(item, float))):
            return(False)
    return(True)

def treatment_not_empty(current_drugs,previous_state_):
    if(bool(current_drugs)==False and previous_state_ !='First time'):
        return(False)
    else:
        return(True)

def patient_EHRs():
    st.markdown("<h1 style='text-align: center; color: #0d325c;'>This web app allows user to create a .json file of his medical data</h1>", unsafe_allow_html = True)

    #Getting patient's name:
    st.subheader("Name:")
    name=st.text_input("enter your name:")

    #Getting Age value:
    st.subheader("Age:")
    age=st.text_input("enter your age:")
    try:
        age= int(age)
    except:
        st.write("Please enter a right value, Age must be a positive number")

    # This function allows us to know whether it's patient's first time to get treatment or already getting
    previous_state_ = previous_state()

    hba1c_records_=hba1c_records(previous_state_)

    hba1c_string=""
    for record in hba1c_records_:
        hba1c_string+=str(record)+"/"
    hba1c_string=hba1c_string[:len(hba1c_string)-1]

    symptoms=symptomatic()
    current_drugs=current_medication(previous_state_)

    current_BMI,current_eGFR,current_UACR=other_analyses_records()
    CVRFs=get_CVRFs(current_BMI, current_eGFR,current_UACR)
    # Let's ask about the clinical condition :
    frailty,heart_failure,established_CVD,hepatic_steatosis,strokes=clinical_cond()

    st.write("#")
    st.write("#")

    if(isinstance(age, int) and treatment_not_empty(current_drugs,previous_state_) and all_hba1czz_are_floats(hba1c_records_)==True and isinstance(current_eGFR, float) and isinstance(current_UACR, float) and isinstance(current_BMI, float) and len(name)>0):
        # Opening JSON file
        with open(full_path, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        st.subheader("Click on the 'Download' button below to create a '.json' file containing all medical informations about this patient !")
        
        json_object["content"][0]["data"]["events"][0]["data"]["items"][0]["value"]["value"]=name
        json_object["content"][0]["data"]["events"][0]["data"]["items"][1]["value"]["value"]=str(age)
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
        col1, col2, col3 = st.columns([4,2,3])
        with col2:
            center_button = st.download_button('Download the ".JSON" file', json_object, file_name=name+str(age)+".json")
        
        if (center_button):
            st.write("#")
            st.write('''
            ## File saved well ✅
            ''')

    else:
        st.subheader("One of the values you entered is invalid, Please check them carefully !")
