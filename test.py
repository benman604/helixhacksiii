# import pandas as pd
# import pickle
# import string
# from sklearn.feature_extraction.text import CountVectorizer
# import nltk
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer as tfidf
# df = pd.read_csv('Data.csv')

# def process_text(text):
    
#     nopunc = [char for char in text if char not in string.punctuation ]
#     nopunc = ''.join(nopunc)
    
#     clean_words = [word for word in nopunc.split() if word.lower not in stopwords.words('english')]
    
#     return clean_words

# def use_model(text):
#     try:
#         df['Message'][df.index[-1]]=text
    
#         messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['Message'])
    
#         pred = model.predict(messages_bow)
#         return pred[-1]

#     except:
#         return 'spam'
    



model = pickle.load(open('finalized_model.sav','rb'))

with open('finalized_model.sav', 'rb') as f:
    model, vectorizer = pickle.load(f)

print(use_model('yo bro wanna go out to eat tmr?'))

#####
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

df = pd.read_csv('fraudTest.csv')

data = df['amt']
numpy_array = data.to_numpy()

x = []

anomalyCount = 0

for loop_var in range(0,len(numpy_array),1):
    x.append(loop_var)


y = numpy_array

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
      return slope * x + intercept

mymodel = list(map(myfunc, x))

for lop in range(0,len(numpy_array),1):
    if (y[lop]-myfunc(lop)>=500):
        # anomalyCount+=1
        print("Anomaly detected at index: ", x[lop])

print(anomalyCount)


plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()