import streamlit as st 
from streamlit_option_menu import option_menu
from json_learning.get_patient_data import patient_EHRs
from Json_files_treat_recommendation.main_treat_recom import main_get_treat

st.set_page_config(page_title="Json stuff", page_icon=":hospital:", layout="centered")

selected=option_menu(
    menu_title="Main Menu",
    options=["Home","Create json","Get Treatment"],
    icons=["house","filetype-json","capsule"],
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

if selected=="Home":
    st.write('#')
    st.write('#')
    st.markdown(
    "<h1 style=' color: #008000;'>Hello! You are in the home page:  </h1>", 
    unsafe_allow_html = True
    )
    st.markdown(
    "<h1 style='color: #000d1a;'>1/Click on 'Create json' to create a Json file in the OpenEHR standards form.  </h1>", 
    unsafe_allow_html = True
    )
    st.markdown(
    "<h1 style='color: #000d1a;'>2/Click on 'Get treatment' to enter your EHRs and get treatment.  </h1>", 
    unsafe_allow_html = True
    )

if selected=="Create json":
    patient_EHRs()
if selected=="Get Treatment":
    main_get_treat()
