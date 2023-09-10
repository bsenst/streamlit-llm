import pandas as pd
import streamlit as st

from utils.tools import load_data, warning

from langchain.llms import Clarifai
from langchain.llms.fake import FakeListLLM
from langchain import PromptTemplate, LLMChain

st.title("Interactive")
warning()
st.caption(f"LLM: {st.secrets.MODEL_ID}")

observations, responses = load_data()

# Initialization
if 'lines' not in st.session_state:
    st.session_state["lines"] = list()

type = st.selectbox("Type", observations.DESCRIPTION.unique())

observations_filtered = observations[observations.DESCRIPTION==type]
if all([value%1==0 for value in observations_filtered.VALUE]):
    values = observations_filtered.VALUE.map(int)
    value_median = int(values.median())
else:
    values = observations_filtered.VALUE
    value_median = values.median()
value_min = values.min()
value_max = values.max()
value = st.slider("Value", min_value=value_min, max_value=value_max, value=value_median)

unit = st.selectbox("Unit", observations_filtered.UNITS.unique())

# Add a button to submit the inputs
if st.button("Add"):
    st.session_state["lines"].append(" ".join([type, str(value), unit]))

observations_selected = st.multiselect(
    'Observations',
    st.session_state.lines,
    default=st.session_state.lines)

template = """A patient has the following list of observations: {observations_selected}\n
Explain the observations in simple language: """

prompt = PromptTemplate(
    template=template, 
    input_variables=["observations_selected"]
) 

llm = Clarifai(pat=st.secrets.CLARIFAI_PAT, user_id=st.secrets.USER_ID, app_id=st.secrets.APP_ID, model_id=st.secrets.MODEL_ID)
llm_chain = LLMChain(prompt=prompt, llm=llm)

if st.button("Submit"):
    st.session_state["output"] = llm_chain.run(", ".join(observations_selected))
    st.write(st.session_state["output"])

if st.button("Reload"):
    st.session_state["lines"] = []
    st.session_state["output"] = ""
    st.experimental_rerun()
