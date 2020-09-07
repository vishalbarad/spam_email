from flask import Flask,render_template,request
import joblib
import numpy as np
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        msg1 = request.form['msg']
        model = joblib.load('Email_Spam_detector.pkl')
        message = model.predict([msg1])[0]
        if message==0:
            ans = "Mail sent successfully"
            return render_template('index.html',ans=ans)
        else:
            ans = "Looking like, you sent a spam email !..."
            return render_template('index.html',ans=ans)


if __name__ == '__main__':
    app.run(debug=True)