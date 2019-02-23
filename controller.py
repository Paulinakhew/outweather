#!usr/bin/env python3

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/mainmenu',methods=['GET'])
def website():
    if request.method=="GET":
        return render_template('index.html', result='hello')
    else:
        return render_template('index.html', result='hello')


if __name__ == '__main__':
    app.run(debug=True)