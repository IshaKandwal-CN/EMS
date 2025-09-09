from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import random

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)  # Email verification flag

    # New fields for OTP
    otp = db.Column(db.String(6), nullable=True)
    otp_expiry = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_otp(self):
        """Generate a 6-digit OTP and set expiry (5 minutes)."""
        self.otp = str(random.randint(100000, 999999))
        self.otp_expiry = datetime.utcnow() + timedelta(minutes=5)
        return self.otp

    def verify_otp(self, otp):
        """Check if OTP matches and is still valid."""
        if self.otp == otp and self.otp_expiry and datetime.utcnow() <= self.otp_expiry:
            self.is_verified = True
            self.otp = None   # Clear OTP after success
            self.otp_expiry = None
            return True
        return False
