from sqlalchemy import create_engine, text
import pymysql
import os

db_connection = os.environ['DB_CONNECTION']
engine = create_engine(db_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs


def load_jobs_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"),
                          {'id': id})
    rows = result.all()
    if len(rows) == 0:
      return None

    else:
      return rows[0]._asdict()


def add_application(job_id, data, file_path):
  with engine.connect() as conn:
    conn.execute(
      text(
        "INSERT INTO applications(job_id, full_name, email,linkedin_url,education,work_experience,resume_url) VALUES (:job_id, :full_name, :email,:linkedin_url,:education,:work_experience,:resume_url)"
      ), {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'work_experience': data['work_experience'],
        'resume_url': file_path,
      })


def save_contactus(data):
  with engine.connect() as conn:
    conn.execute(
      text(
        "INSERT INTO contact(full_name,message,email) VALUES (:full_name, :message,:email)"
      ), {
        'full_name': data['full_name'],
        'email': data['email'],
        'message': data['message'],
      })


def adminlogin(data):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM admin_log WHERE uid=:username AND pass=:password"), {
        'username': data['username'],
        'password': data['password']
      })
    admin = result.fetchone()
    if admin is not None:
      return "true"
    else:
      return "false"

def insertjobs(data):
  with engine.connect() as conn:
    conn.execute(
      text(
        "INSERT INTO jobs(title,location,salary,currency,responsibilities,requirements) VALUES (:jobtitle, :location,:salary,:currency,:responsibilities,:requirements)"
      ), {
        'title': data['jobtitle'],
        'location': data['location'],
        'salary': data['salary'],
         'currency': data['currency'],
        'responsibilities': data['responsibilities'],
        'requirements': data['requirements'],
      })
  
