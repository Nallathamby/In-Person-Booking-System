from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection
def connect_db():
    return pymysql.connect(
        host='pn101.mysql.pythonanywhere-services.com',
        user='pn101',
        password='Cisco123!',  # Your password
        db='pn101$rogers_booking_new',  # Use your correct database name
        cursorclass=pymysql.cursors.DictCursor
    )

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Customer Management (CRUD)
@app.route('/customer', methods=['GET', 'POST'])
def customer():
    connection = connect_db()
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Customer (Name, Email, Phone, Address) VALUES (%s, %s, %s, %s)",
                (request.form['name'], request.form['email'], request.form['phone'], request.form['address'])
            )
            connection.commit()
        connection.close()
        return redirect('/customer')

    # Fetch all customers
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Customer")
        customers = cursor.fetchall()
    connection.close()

    return render_template('customer.html', customers=customers)

@app.route('/customer/delete/<int:id>')
def delete_customer(id):
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Customer WHERE Customer_ID = %s", (id,))
        connection.commit()
    connection.close()
    return redirect('/customer')

@app.route('/customer/edit/<int:id>', methods=['POST'])
def edit_customer(id):
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Customer SET Name=%s, Email=%s, Phone=%s, Address=%s WHERE Customer_ID = %s",
                       (request.form['name'], request.form['email'], request.form['phone'], request.form['address'], id))
        connection.commit()
    connection.close()
    return redirect('/customer')

# Appointment Management (CRUD)
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

    # Fetch all appointments with JOIN to show relevant details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT Appointment.Appointment_ID, Customer.Name AS Customer, Service.Service_Type, Technician.Name AS Technician, 
                   Appointment.Date, Appointment.Time, Appointment.Status
            FROM Appointment
            JOIN Customer ON Appointment.Customer_ID = Customer.Customer_ID
            JOIN Service ON Appointment.Service_ID = Service.Service_ID
            JOIN Technician ON Appointment.Technician_ID = Technician.Technician_ID
        """)
        appointments = cursor.fetchall()
    connection.close()

    return render_template('appointment.html', appointments=appointments)

@app.route('/appointment/delete/<int:id>')
def delete_appointment(id):
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Appointment WHERE Appointment_ID = %s", (id,))
        connection.commit()
    connection.close()
    return redirect('/appointment')

@app.route('/appointment/edit/<int:id>', methods=['POST'])
def edit_appointment(id):
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Appointment SET Status=%s WHERE Appointment_ID = %s",
                       (request.form['status'], id))
        connection.commit()
    connection.close()
    return redirect('/appointment')

if __name__ == '__main__':
    app.run(debug=True)