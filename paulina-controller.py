#!usr/bin/env python3
import requests
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/mainmenu',methods=['GET'])
def website():
    if request.method=="GET":
        return render_template('index.html', result='hello')
    else:
        return render_template('index.html', result='hello')

@app.route('/weather', methods=['GET'])
def weather():
    if request.method=="GET":
        return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)