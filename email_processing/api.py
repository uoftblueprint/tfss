from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from dataclasses import asdict

from models import Email
from config import flask_password

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "tfss_user": flask_password
}


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route('/email', methods=['POST'])
@auth.login_required
def create_email():
    data = request.json

    try:
        email = Email(**data)
        return jsonify(asdict(email)), 200
    except TypeError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
