from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection
def connect_db():
    return pymysql.connect(
        host='your_database_host',
        user='your_database_user',
        password='your_database_password',
        db='your_database_name',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Customer (Name, Email, Phone, Address) VALUES (%s, %s, %s, %s)",
                (request.form['name'], request.form['email'], request.form['phone'], request.form['address'])
            )
            connection.commit()
        connection.close()
        return redirect('/customer')
    return render_template('customer.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    connection = connect_db()
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO Appointment (Customer_ID, Service_ID, Technician_ID, Date, Time, Status)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (request.form['customer_id'], request.form['service_id'], request.form['technician_id'], 
                 request.form['date'], request.form['time'], request.form['status'])
            )
            connection.commit()
        connection.close()
        return redirect('/appointment')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Appointment")
        appointments = cursor.fetchall()
    connection.close()
    return render_template('appointment.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)