#!/usr/bin/env python

import cgi
import cgitb
import sys, urllib
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates', static_url_path='/templates')

@app.route("/")


def main():
    page = request.args.get('page')
    if page != '':
        return render_template(page)
    if page == '':
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
