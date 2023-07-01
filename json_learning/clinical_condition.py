import streamlit as st
import pandas as pd

medium_dose="medium dose"
full_dose= "full dose"
#----------------------------------------------------------------------------------------------

# Let's ask about the clinical condition :
def clinical_cond():
    st.sidebar.title("Clinical condition:")
    
    # frailty:
    frailty = st.sidebar.selectbox(
        "Frailty:",
        ('NO', 'YES'))
    
    # Heart Failure:
    heart_failure = st.sidebar.selectbox(
        "Heart Failure:",
        ('NO', 'YES'))
    
    # Established CVD:
    established_CVD = st.sidebar.selectbox(
        "Established CVD:",
        ('NO', 'YES'))
    
    #Hepatic Steatosis:
    hepatic_steatosis = st.sidebar.selectbox(
        "Hepatic Steatosis:",
        ('NO', 'YES'))
    
    #Strokes:
    strokes = st.sidebar.selectbox(
        "Strokes:",
        ('NO', 'YES'))
    
    return(frailty,heart_failure,established_CVD,hepatic_steatosis,strokes)

#-----------------------------------------------------------------------------------------------------------    
def previous_state():    
    st.subheader("Treatment history:")
    previous_state_ = st.selectbox(
        "Is it your first time to get treatment ?",
        ('First time', 'Second time', 'Two previous times or more'))
    st.write('You selected:', previous_state_)

    # I will add a separation line here
    st.markdown("""---""")
    return(previous_state_)
#------------------------------------------------------------------------------------------------------------------------
def hba1c_records(previous_state_):
    hba1c_records_=[]
    if (previous_state_=='First time'):
        st.subheader("HbA1c(%):")
        current_HbA1c=st.text_input("current HbA1c value:")
        try:
            current_HbA1c= float(current_HbA1c)
        except:
            st.write("Please verifie your HbA1c value !, It must be a number>0!")
        hba1c_records_.append(current_HbA1c)

    elif (previous_state_=='Second time'):
        col_1,col_2=st.columns([1,1])
        with col_1:
            st.subheader("Current HbA1c(%):")
            current_HbA1c=st.text_input("current HbA1c value:")
            try:
                current_HbA1c= float(current_HbA1c)
            except:
                st.write("Please verifie your HbA1c value !, It must be a number>0!")
            hba1c_records_.append(current_HbA1c)
        with col_2:
            st.subheader("Previous HbA1c(%):")
            previous_HbA1c=st.text_input("previous HbA1c value:")
            try:
                previous_HbA1c= float(previous_HbA1c)
            except:
                st.write("Please verifie this value !, It must be a number>0!")
            hba1c_records_.append(previous_HbA1c)
    else:
        col_1, col_2, col_3 = st.columns([1,1,1])
        with col_1:
            st.subheader("Current HbA1c(%):")
            current_HbA1c=st.text_input("current HbA1c value:")
            try:
                current_HbA1c= float(current_HbA1c)
            except:
                st.write("Please verifie your HbA1c value !, It must be a number>0!")
            hba1c_records_.append(current_HbA1c)

        with col_2:
            st.subheader("Previous HbA1c(%):")
            previous_HbA1c=st.text_input("previous HbA1c value:")
            try:
                previous_HbA1c= float(previous_HbA1c)
            except:
                st.write("Please verifie your HbA1c value !, It must be a number>0!")
            hba1c_records_.append(previous_HbA1c)
            
        with col_3:
            st.subheader("HbA1c before previous one:")
            before_previous_HbA1c=st.text_input("before previous HbA1c value:")
            try:
                before_previous_HbA1c= float(before_previous_HbA1c)
            except:
                st.write("Please verifie your HbA1c value !, It must be a number>0!")
            hba1c_records_.append(before_previous_HbA1c)
    st.markdown("""---""")
    
    return(hba1c_records_)
#-----------------------------------------------------------------------------------------------------------------------
def current_medication(previous_state_):
    med_dose_last_time={}  
    if (previous_state_ in['Second time','Two previous times or more']):
        st.subheader("Current treatment")
        last_time_medications = st.multiselect(
                        'Select your current treatment:',
                        ['nonpharmacological therapy', 'Metformin', 'DPP4i', 'SGLT2i', 'Pio', 'SU', 'Basal insulin', 'GLP1RA', 'oral GLP1ra', 'dual GIP/GLP1ra'])
           
        if(len(last_time_medications)==0):
            st.subheader('You selected nothing!')
        else:
            for med_item in last_time_medications:
                if(med_item!='nonpharmacological therapy'):
                    dose_last_time = st.selectbox(
                    'Enter the current dose level of {}?'.format(med_item),
                    (medium_dose,full_dose))
                else:
                    dose_last_time='No specific dose'
                med_dose_last_time[med_item]=dose_last_time
            st.subheader("Below are the drugs you selected:")
            df = pd.DataFrame(list(med_dose_last_time.items()),columns = ['Drug','Dose'])     
            st.dataframe(df,use_container_width=True)
        # I will add a separation line here
        st.markdown("""---""")
    drugs_string=""
    for key,value in med_dose_last_time.items():
        drugs_string+=key+":"+value+"/_/"
    if(len(drugs_string)>0):
        drugs_string=drugs_string[:len(drugs_string)-3]
    return(drugs_string)
#----------------------------------------------------------------------------------------------------
def symptomatic():
    st.subheader("Symptoms :")
    symptoms = st.selectbox(
                "Are you symptomatic now?",
                ('NO', 'YES'))
    if(symptoms=='YES'):
        st.write('You selected: Symptomatic')
    else:
        st.write('You selected: Asymptomatic')    
    st.markdown("""---""")  
    return(symptoms)
#---------------------------------------------------------------------------------------------------------------
def other_analyses_records():
    col001, col002, col003 = st.columns([1,1,1])
    with col001:
        #Getting eGFR value:
        st.subheader("eGFR(ml/min):")
        current_eGFR=st.text_input("enter your current eGFR: estimated glomerular filtration rate (ml/min):")
        try:
            current_eGFR= float(current_eGFR)
        except:
            st.write("Please verify your eGFR value !, It must be a number!")

    with col002:
        #Getting UACR value:
        st.subheader("UACR(mg/g):")
        current_UACR=st.text_input("enter your current UACR: urine albumin/creatinine ratio (mg/g):")
        try:
            current_UACR= float(current_UACR)
        except:
            st.write("Please verify your UACR value !, It must be a number!")        

    with col003:
        #Getting BMI value:
        st.subheader("BMI(Kg/m²):")
        current_BMI=st.text_input("enter your current BMI value (Kg/m²):")
        try:
            current_BMI= float(current_BMI)
        except:
            st.write("Please verify your BMI value !, It must be a number>0!")

    # I will add a separation line here
    st.markdown("""---""")

    return(current_BMI,current_eGFR,current_UACR)
#-----------------------------------------------------------------------------------------
def get_CVRFs(current_BMI, current_eGFR,current_UACR):
    st.subheader("Cardiovascular risk factors:")
    CVRFs = st.multiselect(
                    'Select your cardiovascular risk factors:',
                    ['hypertension','hypercholesterolemia','smoking','albuminuria','family history of early CVD'])
    
    if (isinstance(current_BMI, float)):
        if (current_BMI>=30):
            CVRFs.append('Obesity')

    if (isinstance(current_eGFR, float)):
        if (current_eGFR<60):
            CVRFs.append('eGFR <60 ml/min')

    if (isinstance(current_UACR, float)):
        if (current_UACR>30):
            CVRFs.append('UACR > 30 mg/g')

    if(len(CVRFs)==0):
        st.subheader('You selected nothing!')
    else:
        st.subheader('Here are your cardiovascular risk factors:')
        st.write(CVRFs)

    # I will add a separation line here
    st.markdown("""---""")

    return(CVRFs)
