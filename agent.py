from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
import os

# Setting up the api key
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("api_key")


def create_agent(filename: str):
    """
    Create an agent that can access and use a large language model (LLM).

    Args:
        filename: The path to the CSV file that contains the data.

    Returns:
        An agent that can access and use the LLM.
    """

    # Create an OpenAI object.
    llm = OpenAI(openai_api_key=API_KEY)

    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(filename)
    df['Income'].fillna(0, inplace=True)

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(llm, df, verbose=False)


def query_agent(agent, query):
    """
    Query an agent and return the response as a string.

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """

    prompt = (
        """
        Use the csv file provided to understand the table structure. Then, use the following query to return 
        a SQL query that finds the correct value from the csv. Don't look at the data to make the query. Only look at the
        data structure.

        Return ONLY the sql query and nothing else.

        If you don't know, return I don't know.

        
        Here are some details about the features. If the prompt includes any descriptions, match it to the respective column name and create the sql query.
        AcceptedCmp1: 1 if costumer accepted the offer in the 1* campaign. O otherwise
        AcceptedCmp2: 1 if costumer accepted the offer in the 2nd eampaign, 0 otherwise
        AcceptedCmp3: 1 if costumer accepted the offer in the 3rd campaign, O otherwise
        AcceptedCmp4: 1 if costumer accepted the offer in the 4th campaign, O otherwise
        AcceptedCmp5: 1 if costumer accepted the offer in the 5th campaign, O otherwise
        Response (target): 1 if costumer accepted the offer in the last campaign, O otherwise
        Complain: 1 if costumer complained in the last 2 years
        DtCustomer: date of customer's enrollment with the company
        Education: customer's level of education
        Marital: customer's marital status
        Kidhome: number of small children in customer's household
        Teenhome
        : mumber of teenagers in customer's household
        Income
        :customer's vearly household income
        MntFishProducts
        :amount spent on fish products in the last 2 years
        MntMeat Products
        :amount spent on meat products in the last 2 years
        MntFruits
        :amount spent on fruits in the last 2 vears
        MntSweet :Products amount spent on sweet products in the last 2 years
        Mnt Wines
        :amount spent on wines in the last 2 years
        MntGoldProds
        :amount spent on gold products in the last 2 years
        NumDealsPurchases :number of purchases made with discount
        NumCatalog Purchases :number of purchases made using catalogue
        NumStorePurchases :number of purchases made directly in stores
        Num WebPurchases :number of purchases made through company's web site
        NumWebVisitsMonth :number of visits to company's web site in the last mouth
        Recency
        :mumber of days since the last purchase


        Below is the query.
        Query: 
        """
        + query
    )
    # prompt = (
    #     """
    #         For the following query, if it requires drawing a table, reply as follows:
    #         {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

    #         If the query requires creating a bar chart, reply as follows:
    #         {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
            
    #         If the query requires creating a line chart, reply as follows:
    #         {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
            
    #         There can only be two types of chart, "bar" and "line".
            
    #         If it is just asking a question that requires neither, reply as follows:
    #         {"answer": "answer"}
    #         Example:
    #         {"answer": "The title with the highest rating is 'Gilead'"}
            
    #         If you do not know the answer, reply as follows:
    #         {"answer": "I do not know."}
            
    #         Return all output as a string.
            
    #         All strings in "columns" list and data list, should be in double quotes,
            
    #         For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}
            
    #         Lets think step by step.
            
    #         Below is the query.
    #         Query: 
    #         """
    #     + query
    # )

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response.__str__()
