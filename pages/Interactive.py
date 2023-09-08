import pandas as pd
import streamlit as st

from utils.tools import load_data

from langchain.llms import Clarifai
from langchain.llms.fake import FakeListLLM
from langchain import PromptTemplate, LLMChain
from langchain.output_parsers import CommaSeparatedListOutputParser

st.title("Interactive")

observations, responses = tools.load_data()

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
List the observations out of normal range:{format_instructions}"""

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template=template, 
    input_variables=["observations_selected"],
    partial_variables={"format_instructions": format_instructions}
) 

# llm = Clarifai(pat=st.secrets.CLARIFAI_PAT, user_id=st.secrets.USER_ID, app_id=st.secrets.APP_ID, model_id=st.secrets.MODEL_ID)
responses = ["Abnormal Values:\n* Systolic Blood Pressure\n* Body Temperature\n* ..."]
llm = FakeListLLM(responses=responses)
llm_chain = LLMChain(prompt=prompt, llm=llm)

if st.button("Submit"):
    if "ouput" not in st.session_state:
        st.session_state["output"] = llm_chain.run(", ".join(observations_selected))
    st.write(st.session_state.output)

if st.button("Reload"):
    st.experimental_rerun()
