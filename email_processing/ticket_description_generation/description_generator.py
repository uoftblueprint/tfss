from config import gpt_api_key as api_key
from typing import List, Callable
from dataclasses import dataclass
import openai


@dataclass
class Email:
    to: List[str]
    author: str
    date: str
    subject: str
    body: str


def get_description_from_gpt(input_data: str) -> str:
    """Given some input_data, prompt GPT to return a description."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_data}]
    )
    return response.choices[0].message.content


def construct_basic_prompt(email: Email) -> str:
    """Generates a basic prompt for GPT from the given email."""
    return "Can you generate action items based on this email body:" + email.body


def generate_description(email: Email, construct_prompt: Callable = construct_basic_prompt) -> str:
    """Given the Email object, returns the description of the task as defined in the body of the email."""
    return get_description_from_gpt(construct_prompt(email))


if __name__ == '__main__':
    # for testing purposes
    print(get_description_from_gpt("Hello, I have a question"))
