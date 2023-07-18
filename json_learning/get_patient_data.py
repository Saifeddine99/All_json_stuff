from json_learning.demographics import demographic_data
from json_learning.clinical_data import clinical_data_

from streamlit_option_menu import option_menu

import streamlit as st

def patient_EHRs():

    st.write("#")

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

    if (selected=="Demographic data"):
        demographic_data()
    elif (selected=="Clinical data"):
        clinical_data_()