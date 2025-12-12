from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.model import predict_job
from models.database import init_db, save_prediction, get_stats, get_history

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    fake_count, real_count = get_stats()
    last_history = get_history()[:1]

    job_text = "" 

    if request.method == 'POST':
        job_text = request.form.get('job_description', '').strip()

        if len(job_text) < 50:
            flash("⚠ Please enter a more detailed job description (minimum 50 characters).", "error")
            return render_template(
                'index.html',
                job_text=job_text,   
                fake_count=fake_count,
                real_count=real_count,
                last_prediction=last_history[0] if last_history else None
            )

        
        result, confidence = predict_job(job_text)

        if result in ["Fake Job", "Real Job"]:
            save_prediction(job_text, result, confidence)
            fake_count, real_count = get_stats()

            return render_template(
                'result.html',
                label=result,
                confidence=confidence,
                job_text=job_text,
                fake_count=fake_count,
                real_count=real_count
            )

        else:
            flash("⚠ Prediction failed — please try again.", "error")

    
    return render_template(
        'index.html',
        job_text=job_text,
        fake_count=fake_count,
        real_count=real_count,
        last_prediction=last_history[0] if last_history else None
    )


@main_bp.route('/history')
def history():
    all_history = get_history()
    return render_template('history.html', history=all_history)
