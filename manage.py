
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='temp')
Bootstrap(app)
app.secret_key = "secret key"

conn = mysql.connector.connect(
	host='localhost',
	user='final1',
	password='nohel1',
	database= 'Students'
)

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        StudentID INT AUTO_INCREMENT PRIMARY KEY,
        StudentName VARCHAR(200),
        StudentBDate VARCHAR(200),
        StudentAddress VARCHAR(200))''')
print("Table created")
conn.close()

@app.route('/')
def home():
    return render_template('studenthomepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        StudentName = request.form['StudentName']
        StudentBDate = request.form['StudentBDate']
        StudentAddress = request.form['StudentAddress']

        conn = mysql.connector.connect(
		host='localhost',
		user='final1',
		password='nohel1',
		database= 'Students'
)
        c = conn.cursor()
        c.execute("INSERT INTO Students (StudentName, StudentBDate, StudentAddress) VALUES ('{0}','{1}','{2}','{3}')" , (StudentName, StudentBDate, StudentAddress))
        conn.commit()
        conn.close()

        return redirect(url_for('information'))
    
    return render_template('register.html')

@app.route('/information')
def information():
	conn = mysql.connector.connect(
		host='localhost',
		user='final1',
		password='nohel1',
		database= 'Students'
)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Students")
	rows = cur.fetchall()
	return render_template('information.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
