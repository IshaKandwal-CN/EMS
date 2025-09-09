from app import app
from extensions import db
from models.payroll import Payroll  # ensure model is imported

with app.app_context():
    db.create_all()
    print("Tables created successfully.")