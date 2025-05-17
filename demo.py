import os
from dotenv import load_dotenv, find_dotenv

# Find and load .env file
dotenv_path = find_dotenv()
print("Found .env at:", dotenv_path)
load_dotenv(dotenv_path)

# Read the MongoDB URL
mongo_uri = os.getenv("MONGODB_URL")
print("Mongo URI:", mongo_uri)
