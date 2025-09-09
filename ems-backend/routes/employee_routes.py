from flask import Blueprint, request, jsonify
from extensions import db
from models.employee import Employee
from flask_jwt_extended import jwt_required

employee_bp = Blueprint("employees", __name__)

# Create Employee (only with JWT)
@employee_bp.route("/", methods=["POST"])
@jwt_required()
def add_employee():
    data = request.get_json()
    new_emp = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"],
        role=data.get("role", "Employee"),
        salary=data["salary"]
    )
    db.session.add(new_emp)
    db.session.commit()
    return jsonify({"message": "Employee added!"}), 201

# Get All Employees (only with JWT)
@employee_bp.route("/", methods=["GET"])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    return jsonify([emp.to_dict() for emp in employees]), 200
