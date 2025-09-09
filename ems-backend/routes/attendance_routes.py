from flask import Blueprint, request, jsonify
from extensions import db
from models.attendance import Attendance
from models.employee import Employee
from datetime import datetime
from flask_jwt_extended import jwt_required

attendance_bp = Blueprint("attendance", __name__)

# Add attendance record
@attendance_bp.route("/", methods=["POST"])
@jwt_required()
def add_attendance():
    data = request.get_json()
    employee_id = data.get("employee_id")
    status = data.get("status")
    date_str = data.get("date")

    if date_str:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        date = datetime.utcnow().date()

    emp = Employee.query.get(employee_id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    new_record = Attendance(employee_id=employee_id, status=status, date=date)
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Attendance record added!"}), 201

# Get attendance
@attendance_bp.route("/", methods=["GET"])
@jwt_required()
def get_attendance():
    records = Attendance.query.all()
    return jsonify([r.to_dict() for r in records]), 200
