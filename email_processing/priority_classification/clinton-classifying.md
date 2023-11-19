# Email Dataset
[Hillary clinton private email server](https://raw.githubusercontent.com/Mithileysh/Email-Datasets/master/Hillary%20Clinton%20Datasets/Emails.csv)

# GPT-3.5 Prompt 
```
prompt=f”””

You will be provided with text that is a sequence of emails delimited by triple backticks, we will call this text “email dataset”. Your task is to classify each email’s priority (defined by importance/urgency). 5 for high priority, 1 for low priority. The email dataset is not clean, as it contains a sequences of emails with poor delimiters. The task is NOT to generate code that can do the job, rather, I want you to complete the task. To help you, I have broken down the task for you, please follow them:
1. Extract individual emails from the email dataset. Most commonly, you can separate emails from each other using the email header “From:”, indicating a new email. 
2. For each individual email, notice the structure is split into: 1) email header  2) Email body. To do this, follow these substeps:
	a) Identify these structural components for each email. The email body will not have an explicit label. The body is the text following the subject, before the email sign-off, if any.
	b) Some emails are email chains, which contain past email information when it is forwarded/replied to. These emails will contains multiple email headers. For email chains, try to find the email body of the most recent email in the chain.
3. For each email, based on the email header and body, your task is to label the email with a priority from 1 to 5. The definition of each priority is provided in triple dashes --- below. 
4. Provide your results in csv format with columns: email body, priority 

	```
	{email data}
	```

	---

	### 1. Urgent (Immediate Action Required)
	- Explicit mentions of immediate action, crisis, emergency, or significant negative consequences if not addressed promptly.
	- Phrases implying critical impact on operations, safety, or essential functions. Imminent deadlines within hours or very short terms are mentioned.
	- Indicates that a response or action is required as soon as possible, ideally within the same working day.

	### 2. High (Blockers, ASAP/Same-day Response)
	- Discussions of obstacles or issues impacting ongoing projects or operations that require a timely decision or input.
	- Mentions of approaching deadlines, time-sensitive decisions, or fast-approaching meetings where input or action is crucial.
	- Suggests a need for a response or action by the end of the day or within 24 hours.

	### 3. Medium (Timely Response Required)
	- Routine business inquiries, updates on ongoing projects, requests for information not indicated as urgent.
	- Standard office communications, coordination emails, or follow-ups on previous discussions.
	- No explicit or implied rush, suggesting a response is expected within a reasonable but not immediate timeframe (2-3 days).

	### 4. Low (Non-Urgent/Casual)
	- General information, newsletters, non-urgent updates, casual check-ins, or social invitations related to work.
	- Language indicating that the content is informative or optional rather than necessary for immediate business processes.
	- No immediate response required or expected, can be attended to as per convenience.

	### 5. None (Promotional)
	- Promotional material, advertisements, unsolicited sales pitches, or clearly non-personalized mass emails.
	- Lack of personalization, generic marketing language, offers, or invitations not directly related to immediate work needs.
	- Generally does not require a response or attention unless of specific personal or professional interest.
  	---
"""
```

# Observations
1. GPT is not good at extracting email body content from email chains, where there are many forwards/replies and chains of repeating content and email headers. GPT often misses an emily body if it is in a long email chain. However, it only includes repeated/forwarded email bodies once.
2. After incorporating jeff's priority definitions, the outcomes are not too bad!
[See example here](https://chat.openai.com/share/ed64ed4e-eb3a-4f15-b7aa-d56dbc8388a4)

