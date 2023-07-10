import streamlit as st 
import pandas as pd
import json

def new_med(name,age,proposed_med,next_date):
    # I will add a separation line here
    st.markdown("""---""")      
    #Here we show the proposed medications:           
    st.subheader("Mr {}! Below is your recommended treatment:".format(name))
    df = pd.DataFrame(list(proposed_med.items()),columns = ['recommended_Drug','recommended_Dose'])     
    st.dataframe(df,use_container_width=True)
    #Reminder always shown:
    st.subheader("Always keep aware of these points:")
    st.write("1/Nutrition")
    st.write("2/Physical activity")
    st.write("3/self-management education and support")

    # I will add a separation line here
    st.markdown("""---""")

    #Reminder for user to Check every 3-6 months
    st.subheader("Next check:")
    st.text(next_date)

    st.write("#")
    st.subheader("If you are satisfied with the recommended treatment, Click on the 'Download' button below to save data in the OpenEHR standards form:")
    st.write("#")
    
    json_object={}
    json_object = json.dumps(json_object, indent=4)
    col1, col2, col3 = st.columns([4,2,3])
    with col2:
        download_button = st.download_button('Download', json_object, file_name="recommended_treatment_for_"+name+"_"+str(age)+".json")