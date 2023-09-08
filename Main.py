import os
import pandas as pd
import streamlit as st

title = "LLM supported Observations"

st.set_page_config(
    page_title=title,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/bsenst/streamlit-llm/blob/main/README.md',
        'Report a bug': "https://www.github.com/bsenst/streamlit-llm/issues",
        'About': f"### {title}.\nThis is an exerimental app and not intended for real world use."
    }
)

@st.cache_data
def load_data():
    observations = pd.read_csv("notebooks/csv/observations_processed.csv")
    responses = pd.read_csv("notebooks/csv/observations_responses.csv", sep="#")
    return observations, responses

# Create a Streamlit app
st.title(title)

observations, responses = load_data()

observations = observations[observations.PATIENT.isin(responses.PATIENT)]

# Select a patient from the list
selected_patient = st.selectbox("Select a patient id:", observations["PATIENT"].unique()[:3])

# Display the selected patient's information
if selected_patient:
    st.write(f"You have selected patient id {selected_patient}.")
    
    observations = observations[observations["PATIENT"]==selected_patient]
    responses = responses[responses["PATIENT"]==selected_patient]
    for date in observations.DATE.unique():
        observations_on_date = observations[observations.DATE==date][["DESCRIPTION", "VALUE", "UNITS"]].reset_index(drop=True)
        response = responses[responses.DATE==date].RESPONSE.values[0]
        with st.expander(f"{date}, {len(observations_on_date)} Observations"):
            col1, col2 = st.columns(2, gap="small")

            with col1:
                st.write(observations_on_date)

            with col2:
                st.write(response)