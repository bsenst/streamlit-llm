import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    observations = pd.read_csv("notebooks/csv/observations_processed.csv")
    responses = pd.read_csv("notebooks/csv/observations_responses.csv", sep="#")
    return observations, responses