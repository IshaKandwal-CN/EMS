from flask import Flask
from extensions import db
from config import Config

# Import Blueprints
from routes.employee_routes import employee_bp
from routes.attendance_routes import attendance_bp
from routes.payroll_routes import payroll_bp
from routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from extensions import db, mail  # ✅ make sure mail is imported here
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    CORS(app)

    # Register Blueprints with prefixes
    
    app.register_blueprint(employee_bp, url_prefix="/employees")
    app.register_blueprint(attendance_bp, url_prefix="/attendance")
    app.register_blueprint(payroll_bp, url_prefix="/payroll")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    app.config["JWT_SECRET_KEY"] = "supersecretkey"  # change in production
    jwt = JWTManager(app)


    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

