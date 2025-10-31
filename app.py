from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'scholarships.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # So you can access columns by name
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    category = request.form.get('category')
    stream = request.form.get('stream')

    db = get_db()
    cursor = db.cursor()

    # Query scholarships that match both category and stream if provided
    query = "SELECT * FROM scholarships WHERE 1=1"
    params = []

    if category:
        query += " AND category=?"
        params.append(category)
    if stream:
        query += " AND stream=?"
        params.append(stream)

    cursor.execute(query, params)
    results = cursor.fetchall()
    return render_template('results.html', scholarships=results)

import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)


