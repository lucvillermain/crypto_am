########################################################
######## Application Web pour CRYPTAM ################
########################################################


# La première version du site web sera une application streamlit
# pour sa facilité d'utilisation

# Dans le futur avoir un site web plus développé


import streamlit as st
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

username_entered = st.secrets["username"]   
password_entered = st.secrets["password"]   


st.title('CRYPTAM')

st.sidebar.title("Navigation")
page = st.sidebar.radio("", ("What we do", "Login"))


if page == "What we do" :
    with st.expander('What is CRYPTAM ?'):
      st.write('CRYPTAM is a digital asset manager \
               focused on quantitative trading strategies. \
               We combine macro events with advanced modelling\
               techniques to profit from volatile markets')



elif page == "Login" : 

    st.title("Investors Login")


    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username_entered == username and password_entered == password:
            st.success("Succesful login")
            # Your app code goes here after successful login
            st.write("Welcome back")
        else:
            st.error("Invalid password or username. Please try again.")




