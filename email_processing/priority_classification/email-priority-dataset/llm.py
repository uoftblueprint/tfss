import os
import time
from langchain import OpenAI
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
import tiktoken

load_dotenv(find_dotenv())

encoding = tiktoken.encoding_for_model("gpt-4")

def add_indents(s, n=8):
    # Create a string of n spaces
    indentation = ' ' * n

    # Split the string into lines, add the indentation, then join it back together
    return '\n'.join(indentation + line for line in s.split('\n'))

def append_string_to_file(filename, string):
    with open(filename, 'a') as f:
        f.write(string + '\n')

gpt4 = AzureOpenAI(
    temperature=0,
    model_name="gpt-4",
    deployment_id="gpt-4",
)

def run_prompt(prompt):


    print(f"Prompting with: *****\n{add_indents(prompt)}\n<<<<<")
    start_time = time.time()
    result = gpt4(prompt)
    end_time = time.time()
    elapsed_time = end_time - start_time
    r = f"Response ({elapsed_time} seconds):\n{add_indents(result)}\n<<<<<"
    print(r)
    append_string_to_file("out.txt", r)
    return result

if __name__ == "__main__":
    # print(run_prompt("What is yemen?"))
    prompt = """
Q5 [5pts] Prove that the function halts. Hint: Simplify the variables.

oscillate(happiness):
    patience <- 1/2
    if happiness < patience:
        return "No will to live"
    understanding <- happiness^(patience)
    symmetry <- understanding - patience
    compassion <- understanding + patience
    despair <- symmetry * compassion
    return oscillate(despair)

"""
    print(run_prompt(prompt))
    print(len(encoding.encode(prompt)))