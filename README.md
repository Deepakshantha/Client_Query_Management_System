# 📌 Client Query Management System
A real-time Query Submission & Support Management Dashboard
Built with Python, MySQL, and Streamlit

## 📖 Overview
The Client Query Management System provides a seamless interface for clients to submit queries and for support teams to manage, track, and close them in real time.

This project uses:

* CSV dataset to simulate initial query logs

* MySQL for backend database storage

* Streamlit as the interactive web UI

* Hashed passwords for secure authentication

* Pandas + datetime for data handling and metrics

## 🚀 Features
### 🔐 1. Login & Registration System

* Users can register as Client or Support Team

* Passwords are hashed using SHA-256

* Secure login validation

Role-based navigation:

* Client → Query Submission Page

* Support → Support Dashboard

### 📝 2. Query Submission (Client Side)

Clients can submit queries with:

* Email ID

* Mobile Number

* Query Heading

* Query Description

### 🛠️ 3. Support Team Dashboard

Support agents can:

* View all open/closed queries

* Search queries by keywords

* Filter by status

* Close queries

### Tech Stack

* Frontend : Streamlit
  
* Backend	: Python
  
* Database	: MySQL (mysql-connector-python)
  
* Libraries	: Pandas, datetime, hashlib

* Auth	: SHA-256 hashed passwords

### 🟢 Completed – Ready for review




