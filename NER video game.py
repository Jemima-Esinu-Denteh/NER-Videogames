# -*- coding: utf-8 -*-
"""NLPActivities_(3).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qowYKcK97ZIMy7QHC5YbsCJ7IMEKcnew
"""

import nltk
nltk.download()

import pandas as pd
df = pd.read_csv('Video_games_reviews.csv', delimiter = '\t', header = None)
df

video_review_texts = df[2]
video_review_texts

nltk.download('punkt')

from textblob import TextBlob
for index, review_text in enumerate(video_review_texts):
  blob = TextBlob(review_text)
  print('Analysing review\t' + review_text)
  for sentence in blob.sentences:
    print('------SENTIMENT OF SENTENCE------')
    print(sentence, '\t', sentence.sentiment.polarity)
    print('------END------')

import random
sentiment_classification_labels = []
for index, review_text in enumerate(video_review_texts):
  blob = TextBlob(review_text)
  sentiment_label_for_current_review = random.randint(0,1)
  sentiment_classification_labels.append(sentiment_label_for_current_review)

df['Sentiment_Classfication_Labels'] = sentiment_classification_labels
df
  #print(sentiment_classification_labels)

df[df.Sentiment_Classfication_Labels==0]

df[df.Sentiment_Classfication_Labels==1]

nltk.download('averaged_perceptron_tagger')

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

input_sentence = 'I study at Edge Hill University, which is located in Ormskirk'
chunks = ne_chunk(pos_tag(word_tokenize(input_sentence)))
print(chunks)

for ne in chunks:
  if type(ne) == Tree:
    print(ne)