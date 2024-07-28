from flask import Flask, request, jsonify, render_template
from database import get_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_habit', methods=['POST'])
def add_habit():
    data = request.json
    db = get_db()
    habits_collection = db.habits
    habit = {
        "name": data['name'],
        "frequency": data['frequency'],
        "user": data['user']
    }
    habits_collection.insert_one(habit)
    return jsonify({"message": "Habit added successfully!"})

@app.route('/get_habits/<user>', methods=['GET'])
def get_habits(user):
    db = get_db()
    habits_collection = db.habits
    habits = habits_collection.find({"user": user})
    return jsonify([habit for habit in habits])

if __name__ == '__main__':
    app.run(debug=True)
