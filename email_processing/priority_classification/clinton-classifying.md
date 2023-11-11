# Email Dataset
[Hillary clinton private email server](https://raw.githubusercontent.com/Mithileysh/Email-Datasets/master/Hillary%20Clinton%20Datasets/Emails.csv)

# GPT-3.5 Prompt 
```
prompt=f”””

You will be provided with text that is a sequence of emails delimited by triple backticks, we will call this text “email dataset”. Your task is to classify each email’s priority (defined by importance/urgency). 5 for high priority, 1 for low priority. The email dataset is not very clean, as it contains a sequences of emails with poor delimiters. The task is NOT to generate code that can do the job, rather, I want you to complete the task. To help you, I have broken down the task for you, please follow them:
1. Extract individual emails from the email dataset. Most commonly, you can separate emails from each other using the email header “From:”, indicating a new email. 
2. For each individual email, notice the structure is split into: 1) email header  2) Email body. To do this, follow these substeps:
	a) Identify these structural components for each email. The email body will not have an explicit label. The body is the text following the subject, before the email sign-off, if any.
	b) Some emails are email chains, which contain past email information when it is forwarded/replied to. These emails will contains multiple email headers. For email chains, try to find the email body of the most recent email in the chain.
3. For each email, based on the email header and body, your task is to label the email with a priority from 1 to 5. Here are some things to think about while labelling:
- Are there any action items? Emails with actions have higher priority
- Is the tone urgent? Emails with urgent tones have higher priority.
4. Provide your results in csv format with columns: email body, priority 

	```
	{email data}
	```
"""
```

# Challenges so far
1. GPT is not good at extracting email body content from email chains, where there are many forwards/replies and chains of repeating content and email headers
2. My prompt lacks a definition for priority classification -- what defines an email to be priority 1 to 5?
