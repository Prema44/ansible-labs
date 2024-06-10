import os
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DB'] = 'employee_db'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route('/')
def main():
    return "Welcome to the Flask MySQL app!"

@app.route('/employees')
def get_employees():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()

    # Convert rows to a list of dictionaries
    employees = []
    for row in rows:
        employees.append({'id': row[0], 'name': row[1], 'position': row[2]})

    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
