from app import app
from flask import jsonify
from database.db import get_connection

@app.route('/')
def home():
    return "Hello, Morgan!"

@app.route('/api/cars')
def get_cars():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cars')
    cars = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(cars)


