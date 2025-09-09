from extensions import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Present / Absent / Leave

    # Relationship (optional: allows you to access employee info directly)
    employee = db.relationship("Employee", backref="attendance_records")

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": self.date.strftime("%Y-%m-%d"),
            "status": self.status
        }
