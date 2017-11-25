from flask import Flask, render_template, request
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def home():
    return render_template('store.html')