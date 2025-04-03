CREATE DATABASE rogers_booking;
USE rogers_booking;

CREATE TABLE Customer (
    Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    Address TEXT
);

CREATE TABLE Technician (
    Technician_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Expertise VARCHAR(100),
    Phone VARCHAR(20),
    Availability BOOLEAN
);

CREATE TABLE Service (
    Service_ID INT PRIMARY KEY AUTO_INCREMENT,
    Service_Type VARCHAR(50),
    Description TEXT,
    Estimated_Time INT
);

CREATE TABLE Appointment (
    Appointment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_ID INT,
    Service_ID INT,
    Technician_ID INT,
    Date DATE,
    Time TIME,
    Status ENUM('Scheduled', 'Completed', 'Cancelled'),
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Service_ID) REFERENCES Service(Service_ID),
    FOREIGN KEY (Technician_ID) REFERENCES Technician(Technician_ID)
);

CREATE TABLE Feedback (
    Feedback_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_ID INT,
    Appointment_ID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comments TEXT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID)
);