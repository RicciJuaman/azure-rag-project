import os
from pathlib import Path
from dotenv import load_dotenv

# Force-load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("OPENAI ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("OPENAI DEPLOYMENT:", os.getenv("AZURE_OPENAI_DEPLOYMENT"))
print("OPENAI API VERSION:", os.getenv("AZURE_OPENAI_API_VERSION"))
