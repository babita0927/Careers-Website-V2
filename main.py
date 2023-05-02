from flask import Flask, render_template, jsonify, request, url_for, redirect, flash, get_flashed_messages
from database import load_jobs_db, load_jobs_from_db, add_application, save_contactus, adminlogin, insertjobs
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'secret_key'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}


@app.route('/')
def home():
  jobs = load_jobs_db()
  return render_template('home.html', jobs=jobs)


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/contactus', methods=['POST'])
def contactsave():
  data = request.form
  save_contactus(data)
  return redirect(url_for('home'))


@app.route('/login')
def employer_log():
  return render_template('login.html')


@app.route('/create_account')
def create_account():
  return render_template('create_account.html')


@app.route('/adminlogin', methods=['POST'])
def adminlog():
  data = request.form
  result = adminlogin(data)
  if result == "true":
    return render_template('adminhome.html', data=data)
  else:
    return render_template('login.html',
                           error_msg="Invalid username or password")


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


@app.route('/job/<id>/apply', methods=['GET', 'POST'])
def apply_to_job(id):
  job = load_jobs_from_db(id)
  data = request.form
  message = None
  if request.method == 'POST':
    f = request.files['file']
    file = f.filename
    if f and allowed_file(f.filename):
      f.save('uploads/' + f.filename)
      add_application(id, data, f.filename)
      return render_template('application_submitted.html',
                             apply=data,
                             job=job,
                             file=file)
    else:
      message = "Invalid file type. Only PDF and DOC files are allowed."
      return render_template('jobpage.html', job=job, message=message)


def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/aboutus')
def about():
  return render_template('about.html')


@app.route('/createjobs')
def createjob():
  return render_template('createjobs.html')


@app.route('/insertjobs', methods=['POST'])
def insertjob():
  data = request.form
  insertjobs(data)
  return render_template('createjobs.html')


@app.route('/showallapp')
def allapp():
  return render_template('showall_application.html')


@app.route('/logout')
def logout():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
