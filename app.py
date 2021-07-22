#!/bin/python2.7
from flask import Flask
from flask import request
from flask import render_template,render_template_string
import re
app = Flask(__name__)

@app.route("/")
def index():
    id = str(request.args.get('id'))
    print(id)
    blacklist=["request" , "%" , "\.", "join" , "\d"]

    for i in blacklist:
        if re.search(i,id):
            return "nonono!!!"

    r = render_template_string(render_template("app.html", id=id))
    return r


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "12345"
    app.run(host=host,port=port,debug=True)