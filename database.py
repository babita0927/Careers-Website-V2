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
