from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():

    current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    response = {
        "email address": "georgeavong@gmail.com",
        "current datetime": current_date,
        "GitHub URL": "https://github.com/avonggeorge/HNG12_Internship.git"
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
