import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='week11')
app.secret_key = "key"

conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        EMPID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMPName TEXT,
        EMPGender TEXT,
        EMPPhone TEXT,
        EMPBdate DATE)''')
print("Table has been created")
conn.close()

@app.route('/')
def home():
    return render_template('Home_Page.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        empname = request.form['EMPName']
        empgender = request.form['EMPGender']
        empphone = request.form['EMPPhone']
        empbdate = request.form['EMPBdate']

        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("INSERT INTO employees (EMPName, EMPGender, EMPPhone, EMPBdate) VALUES (?, ?, ?, ?)" , (empname, empgender, empphone, empbdate))
        conn.commit()
        conn.close()

        return redirect(url_for('information_page'))
    
    return render_template('registration_page.html')

@app.route('/information')
def information():
    with sqlite3.connect('employees.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
    return render_template('information_page.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
