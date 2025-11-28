import os 
from dotenv import load_dotenv

load_dotenv()

ollama_model = os.getenv('ollama_model', 'llama3')