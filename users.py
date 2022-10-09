from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash



def register(username, password):
    hash_password = generate_password_hash(password)
    sql = "SELECT username FROM users1 WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        try:
            sql = """INSERT INTO users1 (username, password)
                    VALUES (:username, :password)"""
            db.session.execute(sql, {"username":username, "password":hash_password})
            db.session.commit()
            return True
        except:
            return False
    else:
        return False
    #sql = """SELECT username FROM users WHERE"""
    #secret_password = generate_password_hash(password)
    #sql = """INSERT INTO users (name, password)
    #        VALUES (:name, :password)"""