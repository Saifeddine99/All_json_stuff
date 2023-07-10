import streamlit as st
import datetime

def demongraphic_data():

    st.markdown("<h1 style='color: #0B5345;'>Demographics data:</h1>", unsafe_allow_html = True)
    st.write("#")
    col_1,col_2,col_3=st.columns([2,0.5,2])
    with col_1:
        #Getting patient's name:
        st.subheader("Name:")
        name=st.text_input("enter your name:")
        
        if (len(name)==0):
            st.warning("You entered nothing !")
        st.write("#")

        #Getting patient's address:
        st.subheader("Address:")
        address=st.text_input("enter your address:")
        if (len(address)==0):
            st.warning("You entered nothing !")
        st.write("#")

        #Getting patient's birth day:
        st.subheader("Birthday date:")
        birthday = st.date_input(
            "When\'s your birthday",
            )
        st.write('Your birthday is:', birthday)

    with col_3:
        #Getting patient's name:
        st.subheader("Surame:")
        surname=st.text_input("enter your surname:")
        if (len(surname)==0):
            st.warning("You entered nothing !")
        st.write("#")

        #Getting patient's postal_code:
        st.subheader("Postal Code:")
        postal_code=st.number_input("enter your postal code:",min_value=0,step=1)
        if (postal_code==0):
            st.warning("You entered nothing !")
        st.write("#")

        #Getting patient's DNI:
        st.subheader("DNI:")
        dni=st.text_input("enter your national identifier:")
        if (len(dni)==0):
            st.warning("You entered nothing !")
        elif (correct_dni(dni) is False):
            st.error("Incorrect DNI !")

        st.write("#")

    return(name,surname,address,postal_code,birthday,dni,correct_dni(dni))

def correct_dni(dni):
    try:
        value=int(dni[:8])
    except:
        return(False)
    if(len(dni)==9 and dni[len(dni)-1].isupper() ):
        return(True)
    else :
        return(False)

