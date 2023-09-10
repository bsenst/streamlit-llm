# streamlit-llm

## Architecture

Streamlit caching
Prompt chaining with LangChain

## Run the app

`streamlit run Main.py`

## Data source

https://synthetichealth.github.io

## Discussion & ToDo

* Consider changes of values over time instead of interpreting each time point individually
* Interpret measurements with context (age, gender)
* Different national diagnostic criteria
* Preserving privacy while interacting with LLMs
* Parse LLM output
* Warning labels according to clinical significance of the results

### Hallucinations

> Respiratory rate: This is the number of breaths a person takes per minute. A normal respiratory rate for an adult at rest is between 12 and 20 breaths per minute. In this case, the patient's respiratory rate is 14 breaths per minute, which is slightly higher than normal.

## Reading list

* https://streamlit.io/community/llm-hackathon-2023
* https://discuss.streamlit.io/t/streamlit-llm-hackathon/50618

## Evaluation criteria

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