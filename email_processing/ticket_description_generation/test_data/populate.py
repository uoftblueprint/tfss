from dataclasses import dataclass
from typing import List
import pandas as pd

@dataclass
class Email:
    to: List[str]
    author: str
    date: str
    subject: str
    body: str

def populate_class(filename):
    df = pd.read_csv(filename, sep=';')
    
    emails = []
    #'To', 'From', 'Subject', 'X-To', 'X-From', 'content'
    for index, row in df.iterrows():
        to = row['to']
        author = row['author']
        date = row['date']
        subject = row['subject']
        body = row['body']

        email = Email(to, author, date, subject, body)
        emails.append(email)

    return emails

if __name__ == '__main__':
    email_objects = populate_class('test_data/task_emails.csv')

    # Check if objects have been created
    if email_objects:
        print("Email objects have been created:")
        for email in email_objects:
            print(email)
    else:
        print("No email objects have been created.")
