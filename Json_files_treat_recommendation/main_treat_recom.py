import streamlit as st 
import pandas as pd
import json

from Json_files_treat_recommendation.data_extractor import extract_data
from Json_files_treat_recommendation.no_clinical_conditions.normal_case import normal_case
from Json_files_treat_recommendation.clinical_condition import clinical_condition
from Json_files_treat_recommendation.new_medications import new_med
from Json_files_treat_recommendation.one_clinical_disease.obesity_case import obese
from Json_files_treat_recommendation.one_clinical_disease.elderly_frailty_case import elderly_frailty
from Json_files_treat_recommendation.one_clinical_disease.heart_failure_case import heart_failure_
from Json_files_treat_recommendation.one_clinical_disease.established_cvd_case import established_cvd
from Json_files_treat_recommendation.one_clinical_disease.chronic_kidney_disease import non_critical_chronic_kidney_disease_,critical_chronic_kidney_disease_

def main_get_treat():
    st.markdown("<h1 style='text-align: center; color: #0d325c;'>Treatment Recommendation</h1>", unsafe_allow_html = True)
    st.write('#')
    st.write('#')

    st.subheader("Enter your '.JSON' file from here:")
    json_file=st.file_uploader("",accept_multiple_files=False,type="json")
    if(json_file is not None):
        patient_data = json.load(json_file)
        name,age,obesity,frailty,heart_failure,established_CVD,symptoms,current_UACR,current_eGFR,current_BMI,current_drugs,hba1c_records=extract_data(patient_data)
        
        elderly='YES' if age>75 else 'NO'
        chronic_kidney_disease='NO' if current_eGFR>=60 and current_UACR<=30 else 'YES'

        columns_=["name","age","obesity","frailty","chronic_kidney_disease","heart_failure","established_CVD","symptoms","current_UACR","current_eGFR","current_BMI","hba1c_records","current_drugs"]
        values_=[name,age,obesity,frailty,chronic_kidney_disease,heart_failure,established_CVD,symptoms,current_UACR,current_eGFR,current_BMI,hba1c_records,current_drugs]
        types=[]
        for item in values_:
            types.append(type(item))

        data={"Value":values_,"Type":types}
        st.subheader("Below is {}'s data:".format(name))
        df = pd.DataFrame(data,index=columns_)    
        st.dataframe(df,use_container_width=True)
        
        if(len(hba1c_records)==1):
            previous_state_="First time"
        elif (len(hba1c_records)==2):
            previous_state_="Second time"
        else:
            previous_state_="Two previous times or more"

        # Let's ask about the clinical condition :
        condition=clinical_condition(obesity,elderly,frailty,chronic_kidney_disease,heart_failure,established_CVD,current_eGFR,current_UACR)

        if(condition[0]=='No other clinical conditions'):
            st.title("Fortunately,You are not suffering from any additional disease!")
        elif(condition[0]=='age_or_frailty'):
            st.title('In your case the treatment priority goes for: "{}"'.format(condition[1]))
        else:
            st.title('In your case the treatment priority goes for: "{}"'.format(condition[0]))
        #--------------------------------------------------------------------------------------------------------------------------------------

        if(condition[0]=="No other clinical conditions"):
            proposed_med,next_date=normal_case(previous_state_,hba1c_records,symptoms,current_drugs)
        elif(condition[0]=="obesity"):
            proposed_med,next_date=obese(hba1c_records,previous_state_,current_BMI,current_drugs)
        elif(condition[0]=="age_or_frailty"):
            proposed_med,next_date=elderly_frailty(hba1c_records,previous_state_,current_drugs)   
        elif(condition[0]=="heart_failure"):
            proposed_med,next_date=heart_failure_(hba1c_records,previous_state_,current_drugs)   
        elif(condition[0]=="established_cvd"):
            proposed_med,next_date=established_cvd(hba1c_records,previous_state_,current_drugs)  
        elif(condition[0]=="critical_chronic_kidney_disease"):
            proposed_med,next_date=critical_chronic_kidney_disease_(hba1c_records,previous_state_,current_drugs) #Not_righttttt         
        elif(condition[0]=="non_critical_chronic_kidney_disease"):
            proposed_med,next_date=non_critical_chronic_kidney_disease_(hba1c_records,previous_state_,current_eGFR,current_UACR,current_drugs) #Not_righttttt

        col1, col2, col3 = st.columns([4,2,3])
        with col2:
            center_button = st.button('Done')
        if (center_button):
            new_med(name,proposed_med,next_date)
        else:
            col01, col02, col03 = st.columns([1,4,1])
            with col02:
                st.write("Click on 'Done' once answering all questions !")
    else:
        st.write('#')
        st.write('#')
        st.markdown("<h1 style='text-align: center; color: #0d325c;'>Waiting for the .json file !</h1>", unsafe_allow_html = True)
