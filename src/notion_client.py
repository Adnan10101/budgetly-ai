from notion_client import Client
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.utils.config import NOTION_DATABASE_ID, NOTION_API
import time

def test():
    notion_client = Client(auth =  NOTION_API)
    rows = notion_client.databases.query(database_id = NOTION_DATABASE_ID)

    #category_url = f"https://api.notion.com/v1/pages/65f0be63-9c3a-4d92-86ee-46fdce77897a"
    #category_data = notion_client.pages.retrieve(page_id = "65f0be63-9c3a-4d92-86ee-46fdce77897a")
    #category_name = category_data['properties']['Name']['title'][0]['text']['content']
    #category_name = category_data['properties']
    
    category_id = rows["results"][1]["properties"]["Category"]["relation"][0]["id"]
    category_data = notion_client.pages.retrieve(page_id = category_id)
    category_name = category_data['properties']["Name"]["title"][0]["plain_text"]
    
    
    print(rows["results"][1]["properties"])
    print("cat name",category_name)
    
def insert_data(category_name, name, amount, date):
    notion_client = Client(auth =  NOTION_API)
    rows = notion_client.databases.query(database_id = NOTION_DATABASE_ID)

    #category_name = "Housing"
    categories = notion_client.databases.query(database_id = "17fd7d8577824d42ab0ed90011d7f903")
    category_id = None
    for category in categories["results"]:
        title = category["properties"]["Name"]["title"][0]["text"]["content"]
        print("title ",title)
        if title == category_name:
            category_id = category["id"]
            break
    
    notion_client.pages.create(
        parent = {"database_id":NOTION_DATABASE_ID},
        properties = {
            "Name": {"title": [{"text": {"content": name}}]},
            "Category": {"relation":[{"id":category_id}]},
            "Amount": {"number":amount},
            "Date":{"date":{"start":date}},
        }
    )

# TDOD: ADD A DELETE FEATURE AS WELL IN THE FUTURE
