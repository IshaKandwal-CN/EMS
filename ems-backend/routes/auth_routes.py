from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, mail
from models.user import User
from flask_mail import Message
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

# ---------------- Register Route ----------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email and password are required"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User with this username or email already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password, is_verified=False)
    otp = new_user.generate_otp()

    db.session.add(new_user)
    db.session.commit()

    # Send OTP email
    msg = Message(
        subject="Your OTP for Email Verification - EMS",
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
        recipients=[email],
        body=f"Hi {username},\n\nYour OTP for verifying your account is: {otp}\nThis OTP will expire in 5 minutes."
    )
    mail.send(msg)

    return jsonify({"message": "User registered successfully! Please check your email for OTP."}), 201

# ---------------- Verify OTP Route ----------------
@auth_bp.route("/verify_otp", methods=["POST"])
def verify_otp():
    data = request.get_json()
    email = data.get("email")
    otp = data.get("otp")

    if not email or not otp:
        return jsonify({"error": "Email and OTP are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.is_verified:
        return jsonify({"message": "Email already verified"}), 200

    if user.verify_otp(otp):
        db.session.commit()
        return jsonify({"message": "OTP verified successfully! You can now log in."}), 200
    else:
        return jsonify({"error": "Invalid or expired OTP"}), 400

# ---------------- Login Route ----------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_verified:
        return jsonify({"error": "Email not verified. Please enter OTP."}), 403

    access_token = create_access_token(identity=user.id)
    return jsonify({"message": "Login successful", "token": access_token}), 200
