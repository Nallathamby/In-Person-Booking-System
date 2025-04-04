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

INSERT INTO Service (Service_Type, Description, Estimated_Time) VALUES
('WiFi Installation', 'Install and configure new WiFi routers and modems.', 60),
('Network Troubleshooting', 'Identify and resolve network connectivity issues.', 90),
('WiFi Signal Optimization', 'Enhance WiFi coverage and boost signal strength.', 45),
('Router Replacement', 'Replace existing routers with upgraded models.', 40),
('Network Security Setup', 'Install and configure security protocols for the network.', 70),
('Device Connection Support', 'Assist in connecting new devices to the WiFi network.', 30),
('WiFi Speed Test', 'Measure and analyze the network speed and performance.', 20),
('Home Network Audit', 'Evaluate the home network for improvements and upgrades.', 50),
('Parental Control Setup', 'Configure and enable parental controls on the WiFi.', 35),
('Firmware Update', 'Update router and modem firmware to the latest version.', 25);

INSERT INTO Technician (Name, Expertise, Phone, Availability) VALUES
('Rajinikanth', 'WiFi Installation', '416-123-4567', TRUE),
('Kamal Haasan', 'Network Troubleshooting', '514-987-6543', TRUE),
('Vijay', 'Signal Optimization', '416-234-5678', FALSE),
('Ajith Kumar', 'Router Replacement', '514-876-5432', TRUE),
('Suriya', 'Security Setup', '416-345-6789', TRUE),
('Nayanthara', 'Device Connection Support', '514-765-4321', FALSE),
('Trisha Krishnan', 'Speed Testing', '416-456-7890', TRUE),
('Tamannaah Bhatia', 'Home Network Audit', '514-654-3210', FALSE),
('Keerthy Suresh', 'Firmware Updates', '416-567-8901', TRUE),
('Samantha Ruth Prabhu', 'Parental Control Setup', '514-543-2109', TRUE);



SELECT Appointment.Appointment_ID, Service.Service_Type, Technician.Name AS Technician, 
       Appointment.Date, Appointment.Time, Appointment.Status
FROM Appointment
JOIN Service ON Appointment.Service_ID = Service.Service_ID
JOIN Technician ON Appointment.Technician_ID = Technician.Technician_ID
WHERE Appointment.Customer_ID = 1;