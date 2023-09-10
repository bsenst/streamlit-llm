# streamlit-llm

## Understanding Medical Observations with Large Language Models

The purpose of this application is to test LLM-generated interpretations of medical observations. 
The explanations are generated fully automatically by a large language model. 
This application should be used for experimental purposes only. 
It does not provide support for real world cases and does not replace advice from medical professionals.

https://experimental-clinical-support.streamlit.app/

### Architecture

* Streamlit caching
* Prompting with LangChain
* LLM backend with Clarifai

### Run the app

`streamlit run Main.py`

### Data source

https://synthetichealth.github.io

## Discussion & ToDo

* Consider changes of values over time instead of interpreting each time point individually
* Interpret measurements with context (age, gender)
* Consider different national diagnostic criteria
* Preserving privacy while interacting with LLMs
* Parse LLM output and process for further queries
* Warning labels according to clinical significance of the results

### Problem: Hallucinations

> Respiratory rate: This is the number of breaths a person takes per minute. A normal respiratory rate for an adult at rest is between 12 and 20 breaths per minute. In this case, the patient's respiratory rate is 14 breaths per minute, which is slightly higher than normal.

## Hackathon resources

* https://streamlit.io/community/llm-hackathon-2023
* https://discuss.streamlit.io/t/streamlit-llm-hackathon/50618

### Evaluation criteria

* Inventive
* Error-free
* Public repo
* Hosted on community cloud
* Tools: LangChain, Clarifai, ...
* LLM pain points: transparency, trust, accuracy, privacy, cost reduction, ethics

## Learning resources

* Prompting
    * https://langchain.readthedocs.io/en/latest/
* Monitoring
    * https://github.com/whylabs/langkit
    * https://arize.com/llm/