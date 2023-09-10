import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    observations = pd.read_csv("notebooks/csv/observations_processed.csv")
    responses = pd.read_csv("notebooks/csv/observations_responses.csv", sep="#")
    return observations, responses

def warning():
    st.warning("""The purpose of this application is to test LLM-generated interpretations of medical observations. 
           The explanations are generated fully automatically by a large language model. 
           This application should be used for testing purposes only. 
           It does not provide support for real world cases and does not replace advice from medical professionals.""")