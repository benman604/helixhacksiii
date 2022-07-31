from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import pickle
import string
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer as tfidf
import matplotlib.pyplot as plt
from scipy import stats
df_scams = pd.read_csv('Data.csv')
df_fraud = pd.read_csv('fraudTest.csv')

def process_text(text):
    nopunc = [char for char in text if char not in string.punctuation ]
    nopunc = ''.join(nopunc)
    clean_words = [word for word in nopunc.split() if word.lower not in stopwords.words('english')]
    return clean_words

def use_model(text):
    try:
        df_scams['Message'][df_scams.index[-1]]=text
        messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df_scams['Message'])
        pred = model.predict(messages_bow)
        return pred[-1]
    except:
        return 'spam'

def calculate_credit_anamolies():
    data = df_fraud['amt']
    data1 = df_fraud['merchant']
    numpy_array = data.to_numpy()
    numpy_array1 = data1.to_numpy()

    x = []
    anomalyCount = 0
    for loop_var in range(0,len(numpy_array),1):
        x.append(loop_var)

    y = numpy_array
    names = numpy_array1
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))
    anomoalies = []

    for lop in range(0,len(numpy_array),1):
        if (y[lop]-myfunc(lop)>=10000):
            anomalyCount+=1
            anomoalies.append("You made a purchase from " + str(names[lop]) + "that costed " + str(y[lop]) + ". Please confirm that this is you.")

    # print("You have " + str(anomalyCount) + " anomalies in your transactions.")
    # [print(anomaly) for anomaly in anomoalies]
    return anomoalies
    
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
    ano = []
    if 'anomalies' in request.args:
        ano = request.args.getlist('anomalies')
    return render_template('creditcard.html', anomalies=ano, hasano=len(ano)>0, count=len(ano))

@app.route('/api/scams', methods=['GET'])
def scam_detection():
    msg = request.args["message"]
    res = use_model(msg)
    return redirect(url_for('scamdetector', message=msg, result=res))

@app.route('/api/creditfraud', methods=['GET'])
def fraud_detection():
    ano = calculate_credit_anamolies()
    return redirect(url_for('creditcard', anomalies=ano))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)




