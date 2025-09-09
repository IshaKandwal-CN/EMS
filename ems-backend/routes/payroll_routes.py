from flask import Blueprint, request, jsonify
from extensions import db
from models.payroll import Payroll
from flask_jwt_extended import jwt_required

payroll_bp = Blueprint("payroll", __name__)

# Add payroll record
@payroll_bp.route("/", methods=["POST"])
@jwt_required()
def add_payroll():
    data = request.get_json()
    new_record = Payroll(
        employee_id=data["employee_id"],
        month=data["month"],
        year=data["year"],
        salary_paid=data["salary_paid"]
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Payroll record added!"}), 201

# Get payroll records
@payroll_bp.route("/", methods=["GET"])
@jwt_required()
def get_payroll():
    records = Payroll.query.all()
    return jsonify([p.to_dict() for p in records]), 200
