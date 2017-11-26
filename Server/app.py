from flask import Flask, render_template, request
from model import *
 
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/store')
def store():
	apps_list=select_all_apps()
	return render_template('store.html', apps=apps_list)

@app.route('/apps/<user_id>')
def apps(user_id):
	apps_list=select_all_apps_from_user(user_id)
	return render_template('apps.html', apps=apps_list)


@app.route('/devices/<user_id>')
def devices(user_id):
	devices_list=select_all_devices_from_user(user_id)
	return render_template('devices.html', devices=devices_list)