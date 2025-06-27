#  Hospital Management System (CLI-Based)

This is a **Command-Line Interface (CLI)** based Hospital Management System developed in **Python** with **MySQL** as the backend. It is designed to simulate real-world hospital operations such as managing patients, doctors, appointments, billing, and more — with role-based access for Admin, Receptionist, and Doctor.

---

##  Features

###  Role-Based Logins
- **Admin**
- **Receptionist**
- **Doctor**

###  Admin Functionalities
- Add new patients and doctors
- View doctor list
- Book appointments
- Generate consultation bills
- View today's appointments

###  Receptionist Functionalities
- Add patients
- View doctor list
- Book appointments
- Generate bills
- View today's appointments

###  Doctor Functionalities
- View doctor list (can be extended to include diagnosis, reports, etc.)

---

##  Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Interface:** CLI (Command Line)
- **Modular Structure:** Each feature is broken into separate Python modules

---

##  Folder Structure
├── main.py # Entry point with login menu

├── db_config.py # MySQL connection setup

├── admin_Login.py # Admin login + menu

├── receptionist_Login.py # Receptionist login + menu

├── doctor_login.py # Doctor login + menu

├── patient.py # Patient registration logic

├── doctor.py # Doctor registration + listing

├── appointment.py # Appointment booking logic

├── billing.py # Billing generation

├── reports.py # Today's appointment report

├── models/ # (Optional: where you store SQL procedures or scripts)

└── hospital.sql # (You can include a sample DB schema file here)

---

##  Prerequisites

- Python 3.x
- MySQL server running with a database named `hospital`
- Required stored procedures in MySQL:
  - `AddDoctor`
  - `AddPatient`
- Python modules:  
  Install using:

```bash
pip install mysql-connector-python
