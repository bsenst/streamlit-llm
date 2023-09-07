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
st.title("Patient Overview")

synthea_data = get_synthea_data()

# Select a patient from the list
selected_patient = st.selectbox("Select a patient id:", synthea_data["patients"]["Id"].unique())

def get_overview(keyword):
    tmp = synthea_data[keyword]
    tmp = tmp[tmp["PATIENT"]==selected_patient]
    if len(tmp)==0:
        st.write(f"no {keyword}")
    else:
        with st.expander(keyword.capitalize()):
            for el in tmp.DESCRIPTION.unique():
                st.markdown(f"* {el}")

# Display the selected patient's information
if selected_patient:
    st.write(f"You have selected {selected_patient}.")
        
    get_overview("conditions")
    # get_overview("medications")
    # get_overview("careplans")
    # get_overview("devices")
    # get_overview("encounters")
    # get_overview("immunizations")
    get_overview("observations")
    # get_overview("procedures")
    # get_overview("supplies")
    
    tmp = synthea_data["observations"]
    tmp = tmp[tmp["PATIENT"]==selected_patient]
    tmp = tmp.drop_duplicates()
    st.write(tmp[["DESCRIPTION", "VALUE", "UNITS"]])