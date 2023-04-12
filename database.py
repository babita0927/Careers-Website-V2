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


#def add_application(job_id,application):
