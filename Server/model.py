import sqlite3

db_conn = sqlite3.connect('/home/BajtaStore/ServerDatabase/db-bajtastore.db')

def select_all_apps():
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM apps")

	rows = cur.fetchall()
	return rows

def select_all_devices_from_user(user_id):
	cur = db_conn.cursor()
	cur.execute("SELECT * FROM devices WHERE user_id=?", user_id)

	rows = cur.fetchall()
	return rows