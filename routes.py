from app import app
from flask import render_template, url_for, flash, redirect, request#, session
from form import Registration, Login
#from flask_sqlalchemy import SQLAlchemy
import users, functionalities

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = Registration(request.form)
    if form.validate() and request.method == "POST":
        username = form.username.data
        password = form.password2.data
        role = form.role.data
        if users.register(username, password, role):
            flash("Thank you for joining us.")
            return redirect(url_for("login"))
    return render_template("registration.html", title="Registration", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if users.login(username, password):
            flash("Your login was made successfully.")
            return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)

@app.route("/home")
@app.route("/")
def home():
    themes = functionalities.find_themes()
    thread_count, comment_count = functionalities.count()
    return render_template("home.html", title="Main", themelist=themes,
    thread_count=thread_count, comment_count=comment_count)

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")

@app.route("/new_theme", methods=["GET", "POST"])
def new_theme():
    if users.require_role(2):
        return redirect("/login")
    if request.method == "GET":
        return render_template('newtheme.html', title="New theme")
    if request.method == "POST":
        themename = request.form["themename"]
        answer = functionalities.new_theme(themename)
        if answer == True:
            return redirect("/theme/"+str(themename))
        if answer == "Already exists":
            flash("Theme already exists")
        if answer == "Too long or short":
            flash("Theme name too short or too long")
        else:
            flash("Please try again")
        return redirect("/new_theme")

@app.route("/theme/<themename>/new_post", methods=["GET", "POST"])
def new_thread(themename):
    if users.require_role(1):
        return redirect("/login")
    if request.method == "GET":
        return render_template("newthread.html", title="New thread",
        themename=themename)
    if request.method == "POST":
        threadname = request.form["threadname"]
        message = request.form["message"]
        if 3 <= len(threadname) <= 50:
            if 3 <= len(message) <= 2000:
                thread_id = functionalities.new_post(threadname, themename,
                message)
                return redirect("/theme/"+str(themename)+"/"+str(thread_id[0]))
            else:
                flash("Your post is either too short or long. Please read " \
                    "instructions.")
        else:
            flash("Your post's headline is either too short or long. " \
                "Please read instructions.")
        return redirect("/theme/"+str(themename)+"/new_post")

@app.route("/theme/<themename>", methods=["GET", "POST"])
def show_theme(themename):
    threadlist = functionalities.threads(themename)
    return render_template("threadpage.html", title=themename,
    threadlist=threadlist)

@app.route("/theme/<themename>/<thread_id>", methods=["GET", "POST"])
def postpage(themename, thread_id):
    messagelist = functionalities.messages(thread_id)
    thread_name = messagelist[-1][0]
    user_like, like_count = functionalities.like_check(thread_id)
    if request.method == "GET":
        return render_template('postpage.html', title=thread_name,
        themename=themename, thread_id=thread_id, messagelist=messagelist[0],
        user_like=user_like, like_count=like_count)
    if request.method == "POST":
        if users.require_role(1):
            return redirect("/login")
        message = request.form["message"]
        if 3 <= len(message) <= 2000:
            functionalities.new_message(message, thread_id)
        else:
            flash("Your post is either too short or long. Please " \
                "read instructions.")
        url = "/theme/"+str(themename)+"/"+str(thread_id)
        return redirect(url)

@app.route("/theme/<themename>/<thread_id>/like", methods=["GET", "POST"])
def postpage_like(themename, thread_id):
    if users.require_role(1):
        return redirect("/login")
    functionalities.likes(thread_id)
    url = "/theme/"+str(themename)+"/"+str(thread_id)
    return redirect(url)

@app.route("/theme/<themename>/<thread_id>/<message_id>/remove",
methods=["GET", "POST"])
def remove_comment(themename, thread_id, message_id):
    if users.require_role(2):
        return redirect("/login")
    functionalities.remove_comment(message_id)
    url = "/theme/"+str(themename)+"/"+str(thread_id)
    return redirect(url)

@app.route("/theme/<themename>/<thread_id>/remove", methods=["GET", "POST"])
def remove_thread(themename, thread_id):
    if users.require_role(2):
        return redirect("/login")
    functionalities.remove_thread(thread_id)
    url = "/theme/"+str(themename)
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)