from flask import Flask, render_template, request
from model import *
 
app = Flask(__name__)

@app.route('/')
@app.route('/<user_id>')
def home(user_id):
	if (user_id != NaN)
		apps_list=select_all_apps_from_user(user_id)
	else
		apps_list=NaN
    return render_template('home.html', apps=apps_list)

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/devices/')
@app.route('/devices/<user_id>')
def devices(user_id):
    devices_list=select_all_devices_from_user(user_id)
    return render_template('devices.html', devices=devices_list)