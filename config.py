import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://root:1234@localhost/employee_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Config
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "jwt-secret-string"

    # Flask-Mail Config
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "ikandwal004@gmail.com"      # ✅ your Gmail
    MAIL_PASSWORD = "yuwakfwowilgljpf"           # ✅ your App Password
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    
