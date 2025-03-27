from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# MySQL Database Connection (Update credentials for PythonAnywhere)
db = pymysql.connect(
    host="your-mysql-host",
    user="your-mysql-username",
    password="your-mysql-password",
    database="BookingService",
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM Service")
        services = cursor.fetchall()
    return render_template('services.html', services=services)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        service_id = request.form['service']
        date = request.form['date']
        time = request.form['time']

        with db.cursor() as cursor:
            cursor.execute("INSERT INTO Customer (Name, Email, Phone, Address) VALUES (%s, %s, %s, %s)",
                           (name, email, phone, address))
            db.commit()
            customer_id = cursor.lastrowid
            cursor.execute("INSERT INTO Appointment (Customer_ID, Service_ID, Date, Time) VALUES (%s, %s, %s, %s)",
                           (customer_id, service_id, date, time))
            db.commit()
        
        return redirect(url_for('index'))
    
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM Service")
        services = cursor.fetchall()
    
    return render_template('booking.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
