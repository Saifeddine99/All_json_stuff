from json_files_creation.demographics import demographic_data
from json_files_creation.clinical_data import clinical_data_

from streamlit_option_menu import option_menu

import streamlit as st

def patient_EHRs():

    st.write("#")
    #this option menu allows user to choose the web page he wants to visit https://www.youtube.com/watch?v=hEPoto5xp3k&t=77s&ab_channel=CodingIsFun
    selected=option_menu(
    menu_title="",
    options=["Demographic data","Clinical data"],
    icons=["geo-alt-fill","clipboard2-pulse"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )
    #If the user selects "Demographic data" from the option menu Streamlit will run this "if" condition
    if (selected=="Demographic data"):
        demographic_data()

    #If the user selects "Clinical data" from the option menu Streamlit will run this "if" condition
    elif (selected=="Clinical data"):
        clinical_data_()