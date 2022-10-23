from db import db
from flask import session

def new_theme(themename):
    if 3 <= len(themename) < 50:
        sql = """SELECT name FROM themes WHERE name=:name"""
        result = db.session.execute(sql, {"name":themename})
        name = result.fetchone()
        if not name:
            try:
                sql = """INSERT INTO themes (name)
                        VALUES (:name)"""
                db.session.execute(sql, {"name":themename})
                db.session.commit()
                return True
            except:
                return False
        else:
            return "Already exists"
    else:
        return "Too long or short"

def find_themes():
    sql = """SELECT name FROM themes"""
    result = db.session.execute(sql)
    themes = result.fetchall()
    if not themes:
        return None
    else:
        return themes

def new_post(threadname, themename, message):
    sql = """SELECT id FROM themes WHERE name=:name"""
    result = db.session.execute(sql, {"name":themename})
    theme_id = result.fetchone()
    user_id = session["user_id"]

    sql = """INSERT INTO threads (thread_name, theme_id, creator_id) VALUES""" \
    """ (:thread_name, :theme_id, :creator_id)"""
    db.session.execute(sql, {"thread_name":threadname, "theme_id":theme_id[0],
    "creator_id":user_id})
    db.session.commit()

    sql = """SELECT MAX(id) FROM threads WHERE thread_name=:name"""
    result = db.session.execute(sql, {"name":threadname})
    thread_id = result.fetchone()

    if new_message(message, thread_id[0]):
        return thread_id

def new_message(message, thread_id):
    user_id = session["user_id"]
    sql = """INSERT INTO messages (thread_id, user_id, message) VALUES""" \
    """ (:thread_id, :user_id, :message)"""
    db.session.execute(sql, {"thread_id":thread_id, "user_id":user_id,
    "message":message})
    db.session.commit()
    return True

def threads(themename):
    sql = """SELECT id FROM themes WHERE name=:name AND hidden=0"""
    result = db.session.execute(sql, {"name":themename})
    theme_id = result.fetchone()

    sql = """SELECT id, thread_name FROM threads WHERE theme_id=:theme_id""" \
    """ AND hidden=0"""
    return db.session.execute(sql, {"theme_id":theme_id[0]}).fetchall()

def messages(thread_id):
    sql = """SELECT messages.id, messages.message, users1.username""" \
    """ FROM messages INNER JOIN users1 ON messages.user_id=users1.id""" \
    """ WHERE thread_id=:thread_id AND hidden=0"""
    messages = db.session.execute(sql, {"thread_id":thread_id}).fetchall()

    sql2 = """SELECT thread_name FROM threads WHERE id=:id"""
    result = db.session.execute(sql2, {"id":thread_id})
    thread_name = result.fetchone()
    return messages, thread_name

def likes(thread_id):
    user_id = session["user_id"]
    sql = """INSERT INTO likes (thread_id, user_id)""" \
    """ VALUES (:thread_id, :user_id)"""
    db.session.execute(sql, {"thread_id":thread_id, "user_id":user_id})
    db.session.commit()
    return True

def like_check(thread_id):
    try:
        user_id = session["user_id"]
        sql = """SELECT user_id FROM likes WHERE user_id=:user_id""" \
        """ AND thread_id=:thread_id"""
        result = db.session.execute(sql, {"user_id":user_id,
        "thread_id":thread_id})
        user_like = result.fetchone()
    except:
        user_like = None
    
    if user_like:
        user_like = True
    else:
        user_like = False

    sql = """SELECT COUNT(user_id) FROM likes WHERE thread_id=:thread_id"""
    result = db.session.execute(sql, {"thread_id": thread_id})
    like_count = result.fetchone()

    return user_like, like_count

def remove_comment(message_id):
    sql = """UPDATE messages SET hidden = 1 WHERE id=:message_id"""
    db.session.execute(sql, {"message_id":message_id})
    db.session.commit()

def remove_thread(thread_id):
    sql = """UPDATE threads SET hidden = 1 WHERE id=:id"""
    db.session.execute(sql, {"id":thread_id})
    db.session.commit()

    sql = """UPDATE messages SET hidden = 1 WHERE thread_id=:thread_id"""
    db.session.execute(sql, {"thread_id":thread_id})
    db.session.commit()

def count():
    try:
        user_id = session["user_id"]
        sql = """SELECT COUNT(id) FROM threads WHERE""" \
        """ creator_id=:user_id AND hidden=0"""
        result = db.session.execute(sql, {"user_id":user_id})
        thread_count = result.fetchone()

        sql = """SELECT COUNT(id) FROM messages WHERE""" \
        """ user_id=:user_id AND hidden=0"""
        result = db.session.execute(sql, {"user_id":user_id})
        comment_count = result.fetchone()
        return thread_count, comment_count
    except:
        return 0,0