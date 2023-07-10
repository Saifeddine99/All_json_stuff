import streamlit as st

from json_learning.clinical_condition import clinical_cond,previous_state,hba1c_records,other_analyses_records,current_medication,symptomatic,get_CVRFs

def clinical_data_():
    st.markdown("<h1 style='color: #0B5345;'>Clinical data:</h1>", unsafe_allow_html = True)
    st.write("#")

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

    return(frailty,heart_failure,established_CVD,hepatic_steatosis,strokes,CVRFs,current_BMI,current_eGFR,current_UACR,current_drugs,symptoms,previous_state_,hba1c_records_,hba1c_string)