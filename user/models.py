from flask import Flask
from flask import jsonify
from flask import request
from flask import session
from flask import redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:
    def start_session(self, user):
        del user['password']

        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print("getting sign-up request", request.form)

        # create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existent email
        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400

        # insert into database
        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "unknown error"}), 400

    def logout(self):
        session.clear()
        return redirect('/')

    def login(self):
        print("getting sign-up request", request.form)

        # create the user object
        user = {
            'email': request.form.get('email'),
            'password': request.form.get('password'),
        }

        # look up user in database & verify credentials
        db_user = db.users.find_one({"email": user["email"]})
        if db_user and pbkdf2_sha256.verify(user["password"], db_user["password"]):
            return self.start_session(db_user)

        return jsonify({"error": "Invalid Credentials"}), 400
