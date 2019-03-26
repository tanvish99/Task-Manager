from flask import Flask,jsonify
import pymysql
app=Flask(__name__)

def db():
	conn = pymysql.connect(host='localhost',
						port=8686,user='root',
						password='',
						db='TaskManager')
	cur = conn.cursor()
	return conn,cur

@app.route('/tasks/')
def tasks():
	conn, cur = db()
	tasks = []
	cur.execute("Select * From Tasks")
	for row in cur:
		tasks.append(row)
	return jsonify(tasks)
	
@app.route('/users/')
def users():
	conn, cur = db()
	users = []
	cur.execute("Select * From users")
	for row in cur:
		users.append(row)
	return jsonify(users)

@app.route('/todaystask/')
def compute():
	conn, cur = db()
	tasks = []
	cur.execute("SELECT * FROM Tasks where DATE(uploaded_on) = CURDATE()")
	for row in cur:
		tasks.append(row)
	return jsonify(tasks)

app.run(debug=True)