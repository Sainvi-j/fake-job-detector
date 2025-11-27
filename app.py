from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'super-secret-key-2025'

# Register blueprints
from routes.main import main_bp
from routes.admin import admin_bp

app.register_blueprint(main_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    print("Public App : http://127.0.0.1:5000/")
    print("Admin Login: http://127.0.0.1:5000/admin/login")
    app.run(debug=True)