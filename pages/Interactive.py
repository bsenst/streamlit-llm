import pandas as pd
import streamlit as st

from utils.tools import load_data, warning

import clarifai

from langchain.llms import Clarifai
from langchain.llms.fake import FakeListLLM
from langchain import PromptTemplate, LLMChain

import uuid
import redis
from redis.commands.json.path import Path
from streamlit_feedback import streamlit_feedback

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
if value_min == value_max:
    value_max = 2*value_min
value = st.slider("Value", min_value=value_min, max_value=value_max, value=value_median)

unit = st.selectbox("Unit", observations_filtered.UNITS.unique())

# Add a button to submit the inputs
if st.button("Add"):
    st.session_state["lines"].append(" ".join([type, str(value), unit]))

observations_selected = st.multiselect(
    'Observations',
    st.session_state.lines,
    default=st.session_state.lines)

st.session_state["lines"] = observations_selected

template = """A patient has the following list of observations: {observations_selected}\n
Explain the observations in simple language: """

prompt = PromptTemplate(
    template=template, 
    input_variables=["observations_selected"]
) 

llm = Clarifai(pat=st.secrets.CLARIFAI_PAT, user_id=st.secrets.USER_ID, app_id=st.secrets.APP_ID, model_id=st.secrets.MODEL_ID)
llm_chain = LLMChain(prompt=prompt, llm=llm)

client = redis.Redis(host=st.secrets.REDIS_HOST, port=st.secrets.REDIS_PORT, db=st.secrets.REDIS_DB, password=st.secrets.REDIS_PASSWORD)

if st.button("Submit"):
    st.write(observations_selected)

    st.session_state["output"] = llm_chain.run(", ".join(observations_selected))
    st.write(st.session_state["output"])

    st.caption("Give feedback to let us know what you think. This includes the observations and LLM-output.")
    st.session_state["feedback"] = streamlit_feedback(
        feedback_type="thumbs",
        align="flex-start",
    )
    
    if st.session_state["feedback"]:
        st.session_state["feedback"]["text"] = f'{st.session_state["lines"]}|{st.session_state["output"]}'
        client.json().set(f'user:{uuid.uuid4()}', '$', st.session_state["feedback"])

if st.button("Reload"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
