## Setup

The user will have to go to the code and add the file path to the csv in `interface.py` (line 9).

Then, run the following commands:

- pip install -r requirements.txt
- streamlit run interface.py

## How does this work?

A streamlit webpage will open up where you can write your prompt. Please try to be as specific as possible.

The LLM will take this prompt and return a SQL query. This SQL query is then processed to the csv file and the result is returned to the user.

The LLM as been given the details of each columns so it can create the correct sql query given a particular prompt.
