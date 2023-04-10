from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': "Banglore",
    'salary': '15,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': "Banglore",
    'salary': '10,00,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': "Pune"
  },
]


@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS, company_name='ABC')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
