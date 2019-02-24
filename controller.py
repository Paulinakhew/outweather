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
        cold_footwear = ["Boots", "Hiking Boots"]
        cold_top = ["Jacket", "Parka", ]
        cold_accessories = ["Hat", "Touque", "Mittens", "Gloves", "Scarf", "Thermal Base Layers"]
        cold_bottoms = ["Jeans", "Sweatpants"]

        mild_footwear = ["Running Shoes", "Dress Shoes", ""]
        mild_top = ["T-Shirt", "Long-Sleeve Shirt", "Light Sweatshirt"]
        mild_accessories = []
        mild_bottoms = ["Sweatpants", "Trackpants", "Jeans", "Cargo Pants"]

        snowRain_footwear = ["Boots"]
        snowRain_top = []
        snowRain_accessories = []
        snowRain_bottoms = []

        hot_footwear = []
        hot_top = []
        hot_accessories = []
        hot_bottoms = []

        return render_template('outfits.html', city = submitted_city, result = result)
    
if __name__ == '__main__':
    app.run(debug=True)
