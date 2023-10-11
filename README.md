## Setup

The user will have to go to the code and add the file path to the csv in `interface.py` (line 9).

Then, run the following commands:

- `pip install -r requirements.txt`
- `streamlit run interface.py`

## How does this work?

A streamlit webpage will open up where you can write your prompt. Please try to be as specific as possible.

The LLM will take this prompt and return a SQL query. This SQL query is then processed to the csv file and the result is returned to the user.

The LLM as been given the details of each columns so it can create the correct sql query given a particular prompt.

The LLM used is a basic OpenAI GPT object. Future versions could include working with more Llama 2 - 7B, Falcon and their variants with some hyperparameter tuning. The current version does not inlcude any tuning to the LLM.

## Why did I choose the SQL way?

In my past experience, I've seen that LLMs halluncinate more with csv data. The results from the LLM may not be consistent or accurate when queries start getting complicated and have multiple filtering. However, the LLM is really good at writing SQL queries from scratch and including subqueries or filters.

I tried to leverage this feature of the LLM and ran the SQL query locally in a Sqlite3 database.

### Future Imprvements

If the sql queries generate an incorrect result or an error, we can include functionality to feed the error message back to the LLM to get an improved version of the SQL query. Furthermore, the LLM can also learn (if setup that way).

### Testing Bugs

In some cases, the LLM continues to output its own results instead of the SQL queries. These results might be correct but have a small chance of being wrong. This needs to be tested further and fixed.
