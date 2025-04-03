from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy Database URI
# Replace 'username', 'password', 'host', and 'database_name' with your MySQL details from PythonAnywhere
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://PNallathamby:Cisco123!@PNallathamby.mysql.pythonanywhere-services.com/PNallathamby$rogers_booking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Customer(db.Model):
    Customer_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Address = db.Column(db.Text, nullable=False)

class Technician(db.Model):
    Technician_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Expertise = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Availability = db.Column(db.Boolean, nullable=False)

class Service(db.Model):
    Service_ID = db.Column(db.Integer, primary_key=True)
    Service_Type = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Estimated_Time = db.Column(db.Integer, nullable=False)

class Appointment(db.Model):
    Appointment_ID = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('customer.Customer_ID'), nullable=False)
    Service_ID = db.Column(db.Integer, db.ForeignKey('service.Service_ID'), nullable=False)
    Technician_ID = db.Column(db.Integer, db.ForeignKey('technician.Technician_ID'), nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Time = db.Column(db.Time, nullable=False)
    Status = db.Column(db.String(20), nullable=False)

class Feedback(db.Model):
    Feedback_ID = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('customer.Customer_ID'), nullable=False)
    Appointment_ID = db.Column(db.Integer, db.ForeignKey('appointment.Appointment_ID'), nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    Comments = db.Column(db.Text, nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customers')
def customers():
    customer_data = Customer.query.all()
    return render_template('customers.html', customers=customer_data)

@app.route('/appointments')
def appointments():
    appointment_data = Appointment.query.join(Customer).join(Service).add_columns(
        Appointment.Appointment_ID, Customer.Name, Service.Service_Type,
        Appointment.Technician_ID, Appointment.Date, Appointment.Time, Appointment.Status
    ).all()
    return render_template('appointments.html', appointments=appointment_data)

@app.route('/feedbacks')
def feedbacks():
    feedback_data = Feedback.query.join(Customer).join(Appointment).add_columns(
        Feedback.Feedback_ID, Customer.Name, Appointment.Appointment_ID,
        Feedback.Rating, Feedback.Comments
    ).all()
    return render_template('feedbacks.html', feedbacks=feedback_data)

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)