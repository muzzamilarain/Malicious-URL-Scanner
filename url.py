from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

def sanitization(web):
    web = web.lower()
    token = []
    dot_token = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')
        slash_token = []
        for j in range(0, len(raw1)):
            raw2 = str(raw1[j]).split('.')
            slash_token = slash_token + raw2
        dot_token = dot_token + raw1 + slash_token
    token = list(set(dot_token)) 
    if 'com' in token:
        token.remove('com')
    return token

file_model = "Classifier/pickel_model.pkl"
file_vectorizer = "Classifier/pickel_vector.pkl"

with open(file_model, 'rb') as f_model:
    lgr = pickle.load(f_model)

with open(file_vectorizer, 'rb') as f_vectorizer:
    vectorizer = pickle.load(f_vectorizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    
    usr_inp_sanitized = sanitization(url)
    usr_inp_vectorized = vectorizer.transform(usr_inp_sanitized)
    usr_inp_prediction = lgr.predict(usr_inp_vectorized)[0]

    return render_template('result.html', url=url, prediction=usr_inp_prediction)

if __name__ == '__main__':
    app.run(debug=True)
