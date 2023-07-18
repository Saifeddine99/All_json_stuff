import streamlit as st 
from streamlit_option_menu import option_menu
from json_learning.get_patient_data import patient_EHRs
from Json_files_treat_recommendation.main_treat_recom import main_get_treat
import requests
from streamlit_lottie import st_lottie


from streamlit_cookies_manager import EncryptedCookieManager

st.set_page_config(page_title="Json stuff", page_icon=":hospital:", layout="centered")

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="",
    # You should really setup a long COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    password="",
)
if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

if("user" not in cookies):
    nav_script = """
    <meta http-equiv="refresh" content="0; url='%s'">
    """ % ("https://rdi.behit.net/redgdps/login")
    st.write(nav_script, unsafe_allow_html=True)




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

selected=option_menu(
    menu_title="Main Menu",
    options=["Home","Create json","Get Treatment","Log out"],
    icons=["house","filetype-json","capsule","box-arrow-right"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "16px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
)

lottie_create_json = load_lottieurl("https://lottie.host/1c02cdb3-669b-405d-a2a0-bc60da003400/k757wwytXM.json")
lottie_treatment = load_lottieurl("https://lottie.host/19713cf4-b810-4c41-ac44-a3206e833307/hWghUpQBeJ.json")

if selected=="Home":
    st.write('#')
    st.write('#')
    st.markdown(
    "<h1 style=' color: #0B5345;'>Hello! You are in the home page:  </h1>", 
    unsafe_allow_html = True
    )
    text, anim = st.columns((2, 1))
    with text:
        st.write('#')
        st.subheader("1/Click on 'Create json' to create a Json file in the OpenEHR standards format")
    with anim:
        st_lottie(lottie_create_json, height=200, key="json_creation")

    st.write('#')
    st.write('#')

    with text:
        st.write('#')
        st.write('#')
        st.write('#')
        st.subheader("2/Click on 'Get treatment' to enter your EHRs's json file and get treatment")
    with anim:
        st_lottie(lottie_treatment, height=200, key="teatment_recommendation")


if selected=="Create json":
    patient_EHRs()
if selected=="Get Treatment":
    main_get_treat()
if selected=="Log out":
    cookies.pop("user")
    nav_script = """
    <meta http-equiv="refresh" content="0; url='%s'">
    """ % ("https://rdi.behit.net/redgdps/login")
    st.write(nav_script, unsafe_allow_html=True)
    

