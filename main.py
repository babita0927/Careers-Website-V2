from flask import Flask, render_template, jsonify, request
from database import load_jobs_db, load_jobs_from_db, add_application

app = Flask(__name__)


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


@app.route('/aboutus')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
