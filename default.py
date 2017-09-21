#!/usr/bin/env python

import cgi
import cgitb
import sys, urllib
from flask import Flask, render_template, request
import pymysql



app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/")


# map the inputs to the function blocks

def main():
    page = request.args.get('id')
    if page is not None:
        if page == '0':
           return render_template('index.html')
        if page == '1':
           return render_template('login.html')
    if page is None:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
# define the function blocks


