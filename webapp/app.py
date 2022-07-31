from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import pickle
import string
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer as tfidf
df = pd.read_csv('Data.csv')

def process_text(text):
    
    nopunc = [char for char in text if char not in string.punctuation ]
    nopunc = ''.join(nopunc)
    
    clean_words = [word for word in nopunc.split() if word.lower not in stopwords.words('english')]
    
    return clean_words

def use_model(text):
    try:
        df['Message'][df.index[-1]]=text
    
        messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['Message'])
    
        pred = model.predict(messages_bow)
        return pred[-1]

    except:
        return 'spam'
    
model = pickle.load(open('finalized_model.sav','rb'))
with open('finalized_model.sav', 'rb') as f:
    model, vectorizer = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scamdetector')
def scamdetector():
    msg = None
    res = None
    if 'message' in request.args:
        msg = request.args['message']
        res = request.args['result']
    return render_template('scamdetector.html', msg=msg, res=res, hasres=res is not None)

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/creditcard')
def creditcard():
    return render_template('creditcard.html')

@app.route('/api/scams', methods=['GET'])
def scam_detection():
    msg = request.args["message"]
    res = use_model(msg)
    return redirect(url_for('scamdetector', message=msg, result=res))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)




