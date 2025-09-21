# server/app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from server.helper import serialize

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # or your DB URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models after db is created
from server.models import User  # your User model

@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify({"users": [serialize(user) for user in users]})

if __name__ == "__main__":
    app.run(debug=True)
