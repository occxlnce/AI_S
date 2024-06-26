from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    # Drop the table if it exists
    c.execute('DROP TABLE IF EXISTS responses')
    # Create the table again
    c.execute('''
        CREATE TABLE responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usage TEXT,
            impact TEXT,
            marks_range TEXT,
            hours_per_week TEXT,
            benefit TEXT,
            challenging TEXT,
            grade_improvement TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on application start
init_db()

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    usage = request.form['usage']
    impact = request.form['impact']
    marks_range = request.form['marks_range']
    hours_per_week = request.form['hours_per_week']
    benefit = request.form['benefit']
    challenging = request.form['challenging']
    grade_improvement = request.form['grade_improvement']

    # Insert data into SQLite database
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO responses (usage, impact, marks_range, hours_per_week, benefit, challenging, grade_improvement)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (usage, impact, marks_range, hours_per_week, benefit, challenging, grade_improvement))
    conn.commit()
    conn.close()

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
