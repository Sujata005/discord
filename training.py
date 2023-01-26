import json
import pickle
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer  # stem down the word for example works,working, work etc
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD

lemmatizer=WordNetLemmatizer

intents = json.loads(open('intents.json').read())

words=[]
classes=[]
documents=[]
ignore_letters=['?','!',',','.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list=nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)
