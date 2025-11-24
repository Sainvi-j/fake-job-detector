from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'super-secret-key-2025'

# Register blueprints
from routes.main import main_bp
from routes.admin import admin_bp

app.register_blueprint(main_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)