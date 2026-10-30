from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from openai import OpenAI

load_dotenv()

def get_openai_model():
    return ChatOpenAI(
        model="gpt-5.4-nano",
        api_key=os.getenv("OPENAI_API_KEY"),
        streaming=True,
    )

def get_model():
    return get_openai_model()