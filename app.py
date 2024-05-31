from flask import Flask, render_template, request, flash, \
    session, redirect, url_for, abort
from orm import signIn, registerPerson, getInfo
from ai_api import aiSettings

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods = ["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session["userLogged"]))

    if request.method == "POST":
        sign = signIn(login=request.form["login"], password=request.form["password"])
        if sign[0]:
            session["userLogged"] = sign[1]
            return redirect(url_for('profile', username=session["userLogged"]))
        else:
            flash("Не верный логин или пароль, повторите попытку авторизации")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")


@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        try:
            registerPerson(nickname=request.form["nickname"],
                           login=request.form["login"],
                           password=request.form["password"])
            return redirect(url_for('index'))
        except:
            flash("Ошибка регистрации: Измените данные")
    return render_template('register.html')


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(404)
    info = getInfo(nickname=username)
    return render_template('profile.html', id=info[0][0],
                           nickname=username, login=info[-1],
                           rule=info[0][1], created_on=info[0][2])


@app.route("/chat", methods = ["POST", "GET"])
def chat():
    if 'userLogged' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        for message in aiSettings(user=session['userLogged'], query=request.form["query"]).parser():
            flash(message)

    return render_template('chat.html')


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html')

"""@app.errorhandler(401)
def accessDenied(error):
    redirect(url_for('login'))"""


if __name__ == "__main__":
    app.run(debug=True)