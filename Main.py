import os
import pandas as pd
import streamlit as st

@st.cache_data
def get_synthea_data():
    synthea_data = dict()
    for csv in os.listdir("notebooks/csv"):
        synthea_data[csv[:-4]]=pd.read_csv("notebooks/csv/"+csv)
    return synthea_data

# Create a Streamlit app
st.title("Patient Selector App")

synthea_data = get_synthea_data()

# Select a patient from the list
selected_patient = st.selectbox("Select a patient id:", synthea_data["patients"]["Id"].unique())

# Display the selected patient's information
if selected_patient:
    st.write(f"You have selected {selected_patient}.")
        
    conditions = synthea_data["conditions"]
    conditions = conditions[conditions["PATIENT"]==selected_patient]
    st.write(conditions.DESCRIPTION)
