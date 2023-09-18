# streamlit-llm

## Understanding Medical Observations with Large Language Models

The purpose of this application is to test LLM-generated interpretations of medical observations. 
The explanations are generated fully automatically by a large language model. 
This application should be used for experimental purposes only. 
It does not provide support for real world cases and does not replace advice from medical professionals.

https://experimental-clinical-support.streamlit.app/

### Architecture

![app-architecture-image](https://github.com/bsenst/streamlit-llm/assets/8211411/d5bc2063-b5fb-43ad-9220-8c5d16954024)

* Streamlit caching loaded Synthea synthetic medical data
* Prompting with LangChain PromptTemplate
* LLM served by Clarifai backend

### Run the app

```
pip install -r requirements.txt
streamlit run Main.py
```

### Data source

https://synthetichealth.github.io

## Discussion

* Consider changes of values over time instead of interpreting each time point individually
* Interpret measurements with context (age, gender)
* Consider different national diagnostic criteria
* Preserving privacy while interacting with LLMs
* Parse LLM output and process for further queries
* Warning labels according to clinical significance of the results
* Guardrails to guide user input

### Prompt engineering

* Better prompts = better LLM results https://learnprompting.org/docs/basics/prompt_engineering#what-happens-when-a-prompt-doesnt-work
* Instruction prompts https://learnprompting.org/docs/basics/instructions
* Assigning roles https://learnprompting.org/docs/basics/roles
* Few-shot prompt vs instruction prompt https://learnprompting.org/docs/basics/few_shot#more-on-structure
* CoT Chain-of-Thought https://learnprompting.org/docs/intermediate/chain_of_thought
* Ensembling
    * AMA https://learnprompting.org/docs/reliability/ensembling#ask-me-anything-ama-prompting
    * Diverse Verifier on Reasoning Steps https://learnprompting.org/docs/reliability/ensembling#diverse
* Calibration https://learnprompting.org/docs/reliability/calibration

### Problem: Hallucinations

> Respiratory rate: This is the number of breaths a person takes per minute. A normal respiratory rate for an adult at rest is between 12 and 20 breaths per minute. In this case, the patient's respiratory rate is 14 breaths per minute, which is slightly higher than normal.

> Input: Erythrocyte distribution width [Entitic volume] by Automated count, Platelet distribution width [Entitic volume] in Blood by Automated count
> [...]
> Output: So, in simple terms, these observations are telling us that the red blood cells in this patient's blood are spread out over a pretty big range of sizes, and the machine that counted them got a slightly higher measurement than the manual count.

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

* LLM
    * https://aiplanet.com/learn/llm-bootcamp
* Prompting
    * https://langchain.readthedocs.io/en/latest/
    * https://learnprompting.org/
    * https://apps.cognitiveclass.ai/learning/course/course-v1:IBMSkillsNetwork+AI0117EN+v1
* Monitoring
    * https://github.com/whylabs/langkit
    * https://arize.com/llm/
