import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password, role):
    hash_password = generate_password_hash(password)
    sql = """SELECT username FROM users1 WHERE username=:username"""
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        try:
            sql = """INSERT INTO users1 (username, password, role)
                    VALUES (:username, :password, :role)"""
            db.session.execute(sql, {"username":username,
            "password":hash_password, "role":role})
            db.session.commit()
            return True
        except:
            return False
    else:
        return False

def login(username, password):
    sql = """SELECT password, id, role FROM users1 WHERE username=:username"""
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    session["user_id"] = user[1]
    session["user_name"] = username
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()
    return True

def require_role(level):
    return session["user_role"] < level

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]