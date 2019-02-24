#!usr/bin/env python3
import requests
import model as m

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/mainmenu',methods=['GET'])
def website():
    if request.method=="GET":
        return render_template('mainmenu.html')
    else:
        return render_template('mainmenu.html')

@app.route('/weather', methods=['GET','POST'])
def weather():
    if request.method=="GET":
        return render_template('weather.html')
    else:
        submitted_city = request.form['city']
        result = m.getWeather(submitted_city)
        return render_template('outfits.html', city = submitted_city, result = result)
    
if __name__ == '__main__':
    app.run(debug=True)
