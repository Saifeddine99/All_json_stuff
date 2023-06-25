import streamlit as st 
import pandas as pd

def new_med(name,proposed_med,next_date):
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