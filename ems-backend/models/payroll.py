from extensions import db
from datetime import datetime

class Payroll(db.Model):
    __tablename__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    base_salary = db.Column(db.Float, nullable=False)
    bonus = db.Column(db.Float, default=0.0)
    deductions = db.Column(db.Float, default=0.0)
    date_issued = db.Column(db.Date, default=datetime.utcnow)

    employee = db.relationship("Employee", backref="payrolls")

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "base_salary": self.base_salary,
            "bonus": self.bonus,
            "deductions": self.deductions,
            "date_issued": str(self.date_issued)
        }
