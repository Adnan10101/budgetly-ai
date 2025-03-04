import requests
import json
from datetime import datetime, timedelta
from src.utils.config import OPENROUTER_API

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API}",
    "Content-Type": "application/json"
}

def call_llm(prompt, max_tokens=200):
    payload = {
        "model": "google/gemini-2.0-pro-exp-02-05:free", 
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()
        #print(f"Status Code: {response.status_code}")
        #print(f"Raw Response: {response.text}")

        data = response.json()
        #print(data["choices"][0]["message"]["content"])
        return data["choices"][0]["message"]["content"]
    except requests.RequestException as e:
        print(f"DeepSeek API error: {str(e)}")
        return None
    
def extract_data(text):
    today = datetime.today().strftime("%Y-%m-%d")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    template = f"""
    You are an expert finance tracker. Given a financial transaction statement in natural language, extract the following key details:
    - **Category Name**: The type of expense (e.g., groceries, shopping, food, etc.).
    - **Name**: The store or entity where the transaction happened.
    - **Amount**: The monetary value of the transaction.
    - **Date**: The date of the transaction (if relative like 'yesterday', convert it to YYYY-MM-DD format).

    **Response Format:**  
    Provide the extracted details as a JSON dict object like this:
    {{
      "category_name": "<category>",
      "name": "<store>",
      "amount": <amount>,
      "date": "<YYYY-MM-DD>"
    }}
    Remember to extract the category only from the following set below in the right format
    -   New Category
    -   Housing
    -   Travel 
    -   home
    -   Charity
    -   Food
    -   Groceries
    -   Rent
    -   Shopping
    -   Education
    -   Health & Wellness
    -   Transport
    -   Utilities
    -   Entertainments
    
    ### **Examples:**
    #### Example 1:
    **Input:**  
    "add 100$ worth of groceries for today from walmart."
    **Output:**  
    {{
      "category_name": "Groceries",
      "name": "walmart",
      "amount": 100,
      "date": "{today}"
    }}

    #### Example 2:
    **Input:**  
    "purchase of 50$ on shopping in amazon on 24th feb 2025."
    **Output:**  
    {{
      "category_name": "Shopping",
      "name": "amazon",
      "amount": 50,
      "date": "2025-02-24"
    }}

    #### Example 3:
    **Input:**  
    "i bought 70$ worth of food yesterday at osmos."
    **Output:**  
    {{
      "category_name": "Food",
      "name": "osmos",
      "amount": 70,
      "date": "{yesterday}"
    }}

    Now, extract details from the following statement:
    "{text}"
    """

    response = call_llm(template)
    cleaned_response = response.replace("json", "", 1).replace("```","",2).strip()
    response_dict = json.loads(cleaned_response)
    return response_dict
    
    # if response:
    #     try:
    #         return json.loads(response)  # Convert the output into a Python dictionary
    #     except json.JSONDecodeError:
    #         print("LLM response is not valid JSON. Here is the raw output:", response)
    #         return None
    # return None