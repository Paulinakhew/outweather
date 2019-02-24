#!usr/bin/env python3
import requests
import random
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
        cold_footwear = ["Boots", "Hiking Boots", "Uggs", "Winter Moccasins"]
        cold_top = ["Jacket", "Parka", ]
        cold_accessories = ["Hat", "Touque", "Mittens", "Gloves", "Scarf", "Thermal Base Layers"]
        cold_bottoms = ["Jeans", "Sweatpants", "Leggings", "Jeggings"]

        mild_footwear = ["Running Shoes", "Dress Shoes", "Slip-On Casual Shoes"]
        mild_top = ["T-Shirt", "Long-Sleeve Shirt", "Light Sweatshirt", "Jean Jacket", "Dress Shirt"]
        mild_accessories = ["Baseball Cap", "Sunglasses"]
        mild_bottoms = ["Sweatpants", "Trackpants", "Jeans", "Cargo Pants", "Dress Pants", "Leggings"]

        snowRain_footwear = ["Boots", "Hiking Shoes", "Rain Boots"]
        snowRain_top = ["Jacket", "Parka", ]
        snowRain_accessories = ["Hat", "Touque", "Gloves", "Scarf"]
        snowRain_bottoms = ["Sweatpants", "Jeans", "Leggings", ]

        hot_footwear = ["Flip-Flops", "Sandals", "Slides", "Running Shoes", "Slip-On Casual Shoes"]
        hot_top = ["Tank Top", "T-Shirt", "Undershirt"]
        hot_accessories = ["Fan", "Water Bottle"]
        hot_bottoms = ["Shorts", "Cargo Shorts", "Jean Shorts", "Trackpants", "3/4 Length Trackpants", ]

        return render_template('outfits.html', city = submitted_city, result = result)
    
if __name__ == '__main__':
    app.run(debug=True)
