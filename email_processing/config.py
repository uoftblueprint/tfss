from dotenv import load_dotenv
import os

load_dotenv()
gpt_api_key = os.getenv("OPENAI_API_KEY")
flask_password = os.getenv("FLASK_PASSWORD")
