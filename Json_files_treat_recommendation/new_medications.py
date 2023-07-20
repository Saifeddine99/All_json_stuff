import streamlit as st 
import pandas as pd

import os
import json

def new_med(proposed_med,next_date):

    # I will add a separation line here
    st.markdown("""---""")      

    #Here we show the proposed medications:           
    st.subheader("Below is your recommended treatment:")
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
    #'MedicationRecommendation.v0-composition.example.json' is the form of file we will follow in saving new recommended treatment 
    full_path = os.path.join('Json_files_treat_recommendation', 'MedicationRecommendation.v0-composition.example.json')

    # Opening JSON file
    with open(full_path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #Here we are addding the new treatment to the file 
    for number in range(len(df)):
        drug=df['recommended_Drug'][number]
        dose=df['recommended_Dose'][number]

        if number<6:
            json_object["content"][0]["data"]["events"][number]["data"]["items"][0]["value"]["value"]=drug
            json_object["content"][0]["data"]["events"][number]["data"]["items"][9]["value"]["value"]=dose
        

    json_object = json.dumps(json_object, indent=4)

    col1, col2, col3 = st.columns([4,2,3])
    with col2:
        #This is a download button that allows to download the created new treatment file 
        download_button = st.download_button('Download', json_object, file_name="recommended_treatment.json")
    
    if (download_button):
        st.write("#")
        st.success(": File saved well" ,icon="✅")