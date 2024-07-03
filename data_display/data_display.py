from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('display.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    name = request.form['name']
    birthdate_str = request.form['birthdate']
    
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return jsonify({'name': name, 'age': age})
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD.'})

if __name__ == '__main__':
    app.run(debug=True)
