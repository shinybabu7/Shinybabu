# -*- coding: utf-8 -*-
"""23BCE20080_IBM_Project_(car_rental)
Original file is located at
    https://colab.research.google.com/drive/1HJOOIi7uGxUiTqYWjNpIJBBXWDHc28K5
"""

!pip install transformers
!pip install pandas
!pip install nltk

import pandas as pd
import torch
from transformers import pipeline
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

from google.colab import files
uploaded = files.upload()

df = pd.read_csv(next(iter(uploaded)))
df.head()

sentiment_model = pipeline("sentiment-analysis")

def get_sentiment(text):
    try:
        result = sentiment_model(text[:512])[0]  # truncate if too long
        return result['label'], result['score']
    except:
        return "ERROR", 0

df[['Sentiment', 'Confidence']] = df['Review'].apply(lambda x: pd.Series(get_sentiment(str(x))))
df.head()

keywords = {
    "Late Delivery": ["late", "delay", "waited", "not on time"],
    "Car Condition": ["dirty", "broken", "damage", "no AC", "scratch"],
    "Customer Service": ["rude", "unhelpful", "support", "behavior"],
    "Billing Issues": ["extra charge", "wrong bill", "overcharged"]
}

def extract_issues(text):
    found_issues = []
    for issue, words in keywords.items():
        if any(word in text.lower() for word in words):
            found_issues.append(issue)
    return ", ".join(found_issues) if found_issues else "None"

df['Detected Issues'] = df['Review'].apply(extract_issues)
df.head()

df.to_csv("Analyzed_Customer_Feedback.csv", index=False)
files.download("Analyzed_Customer_Feedback.csv")

def get_sentiment(text):
    try:
        result = sentiment_model(text[:512])[0]  # truncate if too long
        return result['label'], result['score']
    except:
        return "ERROR", 0

df[['Sentiment', 'Confidence']] = df['Review'].apply(lambda x: pd.Series(get_sentiment(str(x))))
df.head()
