<h3>Employee Management System (EMS)<h3>
<br>

A full-stack Employee Management System built with Flask (Python), MySQL, and a simple HTML/CSS/JS frontend.
Includes secure user authentication with email OTP verification, employee records, attendance tracking, and payroll management.

🔑 Features

User registration & login with JWT authentication

Email OTP verification for secure signup

Manage employees, attendance, and payroll

Responsive frontend with HTML, CSS, and JS

RESTful APIs built using Flask Blueprints

🛠️ Tech Stack

Backend: Flask, SQLAlchemy, Flask-Mail, Flask-JWT-Extended

Database: MySQL

Frontend: HTML, CSS, JavaScript

Other: OTP-based email verification, JWT tokens, CORS enabled

🚀 Getting Started

Clone the repo:

git clone https://github.com/your-username/ems.git
cd ems


Install dependencies:

pip install -r requirements.txt


Set up MySQL and update config.py.

Run the server:

python app.py


Open frontend (signup.html / login.html) in browser.

📧 Email OTP Flow

Register → Get OTP on email → Enter OTP → Verified → Login
