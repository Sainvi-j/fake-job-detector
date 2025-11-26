from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.model import predict_job
from models.database import init_db, save_prediction, get_stats, get_history

main_bp = Blueprint('main', __name__)

@main_bp.route('/index', methods=['GET', 'POST'])
def index():
    init_db()
    fake_count, real_count = get_stats()
    last_history = get_history()[:1]
    
    if request.method == 'POST':
        job_text = request.form.get('job_description', '').strip()
        if len(job_text) < 50:
            flash("Please enter a longer job description.", "error")
        else:
            result, confidence = predict_job(job_text)
            if result != "Invalid":
                save_prediction(job_text, result, confidence)
                return render_template('result.html', 
                                     result=result, 
                                     confidence=confidence, 
                                     job_text=job_text,
                                     fake_count=get_stats()[0],
                                     real_count=get_stats()[1])
            else:
                flash("Invalid input.", "error")
    
    return render_template('index.html', 
                         fake_count=fake_count, 
                         real_count=real_count,
                         last_prediction=last_history[0] if last_history else None)

@main_bp.route('/history')
def history():
    history = get_history()
    return render_template('history.html', history=history)