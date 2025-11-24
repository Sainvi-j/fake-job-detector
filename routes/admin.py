from flask import Blueprint, render_template, request, session, redirect, url_for
from models.database import get_stats, get_chart_data, get_history

admin_bp = Blueprint('admin', __name__)

def login_required(f):
    def wrap(*args, **kwargs):
        if session.get('logged_in'):
            return f(*args, **kwargs)
        return redirect(url_for('admin.login'))
    wrap.__name__ = f.__name__
    return wrap

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('admin.dashboard'))
    return render_template('admin_login.html')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    pie_data, line_data = get_chart_data()
    history = get_history()
    fake, real = get_stats()
    return render_template('admin_dashboard.html', 
                         pie_data=pie_data, 
                         line_data=line_data,
                         history=history,
                         total=fake+real)

@admin_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main.index'))