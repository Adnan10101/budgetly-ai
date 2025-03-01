import os
from dotenv import load_dotenv

# Get the absolute path to the root directory (two levels up from config.py)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Load the .env file from the root directory
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Access variables
OPENROUTER_API = os.getenv("OPENROUTER_API")
NOTION_API = os.getenv("NOTION_API")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PINECONE_API = os.getenv("PINECONE_API")
