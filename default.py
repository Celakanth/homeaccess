#!/usr/bin/env python

import cgi
import cgitb
import sys, urllib
from flask import Flask, render_template, request, session, redirect, url_for, escape
from subprocess import call
import pymysql

sys.setrecursionlimit(2000)

app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.config["DEBUG"] = True
# app.secret_key = "ismine"
comments = []


@app.route("/", methods=["GET", "POST"])
# map the inputs to the function blocks

def main():
    page = request.args.get('id')
    if page is not None:
        if page == '0':
            return render_template('index.html', comments=str(sys.getrecursionlimit()))
        if page == '1':
            if request.method == "POST":
                comments.append(request.form["demo-name"])
                session["username"] = comments
                if comments == "celakanth":
                    return render_template("message.html")
                if 'username' in session:
                    comments.append(escape(session['username']))
                if comments.count("celakanth") > 0:
                    return render_template("message.html")
            else:
                return render_template('login.html')
    if page is None:
        if 'username' in session:
            if request.method == "POST":
                comments.append(escape(session['username']))
                message = request.form["message"]
                call(["espeak", "-a", "50", message])
                return render_template("message.html")
            else:
                return render_template("message.html")

    return render_template('index.html')


app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

if __name__ == "__main__":
    app.run()
# define the function blocks
