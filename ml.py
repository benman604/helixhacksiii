import numpy as np
import pandas as pd
import nltk 
from nltk.corpus import stopwords
import string

df = pd.read_csv('spam.csv', encoding='ISO-8859-1')
df.drop_duplicates(inplace= True)

nltk.download('stopwords')
def cleaner(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

from sklearn.feature_extraction.text import CountVectorizer
messages_bow = CountVectorizer(analyzer=cleaner).fit_transform(df['v2'])
print(type(df['v2']))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['v1'], test_size = 0.2)
print(type(X_test))

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(X_train, y_train)

from sklearn.metrics import accuracy_score
pred = classifier.predict(X_test)
print(accuracy_score(y_test, pred))

import pickle
filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))
pickle.dump(X_test, open('X_test.sav', 'wb'))