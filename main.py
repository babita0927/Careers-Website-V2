from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import load_jobs_db, load_jobs_from_db, add_application
from forms import ApplicationForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

csrf = CSRFProtect(app)


@app.route('/')
def home():
  jobs = load_jobs_db()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  job = load_jobs_from_db(id)
  if not job:
    return "Not Found, 404"
  else:
    return render_template('jobpage.html', job=job)


@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):
  job = load_jobs_from_db(id)
  if not job:
    return "Not Found, 404"
  form = ApplicationForm()
  if form.validate_on_submit():
    data = form.data
    add_application(id, data)
    return render_template('application_submitted.html', apply=data, job=job)
  return render_template('jobpage.html', job=job, form=form)


@app.route('/aboutus')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
