CREATE DATABASE BookingService;
USE BookingService;

CREATE TABLE Customer (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) UNIQUE NOT NULL,
    Address TEXT NOT NULL
);

CREATE TABLE Service (
    Service_ID INT AUTO_INCREMENT PRIMARY KEY,
    Service_Type VARCHAR(50) NOT NULL,
    Description TEXT NOT NULL
);

CREATE TABLE Appointment (
    Appointment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Service_ID INT NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Service_ID) REFERENCES Service(Service_ID)
);
