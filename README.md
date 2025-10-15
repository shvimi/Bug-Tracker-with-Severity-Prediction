# Bug-Tracker-with-Severity-Prediction
A Flask web app for tracking bugs with automatic severity prediction.
A simple Flask web application for tracking software bugs.  
It uses a **rule-based AI** to automatically predict the severity of each bug.

Features
- Report and view bugs
- Auto severity prediction (Low, Medium, High)
- Manage bug details (status, reporter, assignee)
- SQLite database for storage
- Flask & SQLAlchemy backend

---

Tech Stack
- **Python** (Flask, SQLAlchemy)
- **HTML / CSS** (Frontend)
- **SQLite** (Database)

Setup Instructions
bash
 Clone the repository
git clone https://github.com/<shvimi/>/BugTracker.git
cd BugTracker

Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

Install dependencies
pip install -r requirements.txt

 Run the app
python app.py
Access it on http://127.0.0.1:5000/
