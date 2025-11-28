from flask import Blueprint, render_template, request, session, redirect, url_for
from models.database import get_stats, get_chart_data, get_history
from functools import wraps

admin_bp = Blueprint('admin', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('admin.dashboard'))
    return render_template('admin_login.html')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    fake_count, real_count = get_stats()       
    pie_data, line_data = get_chart_data()
    history = get_history()
    
    total = fake_count + real_count
    accuracy = round((real_count * 100 / total), 1) if total > 0 else 0

    dates = [str(row[0]) for row in line_data]
    counts = [row[1] for row in line_data]

    return render_template(
        "admin_dashboard.html",
        fake_count=fake_count,
        real_count=real_count,
        total=total,
        accuracy=accuracy,      # <--- send accuracy correctly
        dates=dates,
        counts=counts,
        history=history
    )



@admin_bp.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main.index'))
