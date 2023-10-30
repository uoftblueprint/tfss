from config import gpt_api_key as api_key
from typing import List
from dataclasses import dataclass

@dataclass
class Email:
    to: List[str]
    author: str
    date: str
    subject: str
    body: str

# TODO: create a function to prompt chatGPT given some input


# TODO: create a function that when inputted some email object, 
# prompts chatGPT and returns the description of a task defined from the email
