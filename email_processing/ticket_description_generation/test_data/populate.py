import csv
from dataclasses import dataclass
from typing import List
import os, sys, email
import numpy as np
import pandas as pd

@dataclass
class Email:
    to: List[str]
    author: str
    date: str
    subject: str
    body: str

def populate_class(filename):
    df = pd.read_csv(filename, sep='\t')
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
    populate_class('your_file.csv')