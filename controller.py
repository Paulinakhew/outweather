#!usr/bin/env python3
import requests
import random
from datetime import datetime
from flask_humanize import Humanize
import model as m

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'paulina is cool'

HUMANIZE_USE_UTC = True

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
    elif request.method=="POST":
        submitted_city = request.form['city']
        check_valid_city = m.check_status_code(submitted_city)
        
        if check_valid_city == True:
            session['submitted_city'] = submitted_city
            return redirect('/outfits')
        else:
            return redirect('/weather')


@app.route('/outfits', methods=['GET','POST'])
def outfits():
    if request.method=="GET":
    
        submitted_city = session.get('submitted_city', None)
        result = m.getWeather(submitted_city)
        random.seed(datetime.now())
        random_num = random.randint(0, 4)
        
        cold_footwear = ["Boots", "Hiking Boots", "Uggs", "Winter Moccasins", "Leather Shoes"]
        cold_top = ["Jacket", "Parka", "Overcoat", "Jacket Shell", "Fur Coat"]
        cold_accessories = ["Hat", "Touque", "Mittens", "Gloves", "Scarf", "Thermal Base Layers"]
        cold_bottoms = ["Jeans", "Sweatpants", "Leggings", "Jeggings", "Khakis"]

        mild_footwear = ["Running Shoes", "Dress Shoes", "Slip-On Casual Shoes", "Slides", "Heels"]
        mild_top = ["T-Shirt", "Long-Sleeve Shirt", "Light Sweatshirt", "Jean Jacket", "Dress Shirt"]
        mild_accessories = ["Baseball Cap", "Headband", "Parasol", "Bucket Hat", "Watch"]
        mild_bottoms = ["Sweatpants", "Long Skirt", "Jeans", "Cargo Pants", "Dress Pants", "Leggings"]

        hot_footwear = ["Flip-Flops", "Sandals", "Slides", "Running Shoes", "Slip-On Casual Shoes"]
        hot_top = ["Tank Top", "T-Shirt", "Undershirt", "Polo", "Blouse"]
        hot_accessories = ["Fan", "Water Bottle", "Sunscreen", "Parasol", "Sunglasses"]
        hot_bottoms = ["Short Skirt", "Cargo Shorts", "Jean Shorts", "Trackpants", "Athletic Shorts"]

        jackets = ["Jacket", "Parka", "Overcoat", "Jacket Shell", "Fur Coat", "Jean Jacket"]
        t_shirt = ["T-Shirt", "Tank Top", "Undershirt", "Polo"]
        long_sleeve_shirt = ["Long-Sleeve Shirt", "Light Sweatshirt", "Dress Shirt", "Blouse"]

        boots = ["Boots", "Hiking Boots", "Uggs", "Leather Shoes"]
        joggers = ["Running Shoes", "Slip-On Casual Shoes"]
        sandals = ["Slides", "Flip-Flops", "Sandals"]
        miscellanouse_shoes = ["Winter Moccasins", "Dress Shoes", "Heels"]

        full_length = ["Jeans", "Sweatpants", "Leggings", "Jeggings", "Khakis", "Long Skirt", "Cargo Pants", "Dress Pants", "Trackpants"]
        half_length = ["Short Skirt", "Cargo Shorts", "Jean Shorts", "Athletic Shorts"]

        weather = ["Thunderstorm", "Drizzle", "Rain", "Snow", "Atmosphere", "Clear", "Clouds"]


        return render_template('outfits.html', city = submitted_city, result = result, randomInt = random_num, coldFootwear = cold_footwear,
        coldBottoms = cold_bottoms, coldTop = cold_top, coldAccessories = cold_accessories,
        mildFootwear = mild_footwear, mildTop = mild_top, mildAccessories = mild_accessories, mildBottoms = mild_bottoms,
        hotFootwear = hot_footwear, hotTop = hot_top, hotAccessories = hot_accessories, hotBottoms = hot_bottoms, 
        jacketsIcon = jackets, tShirtIcon = t_shirt, longSleeveIcon = long_sleeve_shirt, bootsIcon = boots,
        joggersIcon = joggers, sandalsIcon = sandals, miscShoes = miscellanouse_shoes, weather = weather, longPants = full_length,
        shortPants = half_length)
    else:
        submitted_city = session.get('submitted_city', None)
        result = m.getWeather(submitted_city)
        random.seed(datetime.now())
        random_num = random.randint(0, 4)
        
        cold_footwear = ["Boots", "Hiking Boots", "Uggs", "Winter Moccasins", "Leather Shoes"]
        cold_top = ["Jacket", "Parka", "Overcoat", "Jacket Shell", "Fur Coat"]
        cold_accessories = ["Hat", "Touque", "Mittens", "Gloves", "Scarf", "Thermal Base Layers"]
        cold_bottoms = ["Jeans", "Sweatpants", "Leggings", "Jeggings", "Khakis"]

        mild_footwear = ["Running Shoes", "Dress Shoes", "Slip-On Casual Shoes", "Slides", "Heels"]
        mild_top = ["T-Shirt", "Long-Sleeve Shirt", "Light Sweatshirt", "Jean Jacket", "Dress Shirt"]
        mild_accessories = ["Baseball Cap", "Headband", "Parasol", "Bucket Hat", "Watch"]
        mild_bottoms = ["Sweatpants", "Long Skirt", "Jeans", "Cargo Pants", "Dress Pants", "Leggings"]

        hot_footwear = ["Flip-Flops", "Sandals", "Slides", "Running Shoes", "Slip-On Casual Shoes"]
        hot_top = ["Tank Top", "T-Shirt", "Undershirt", "Polo", "Blouse"]
        hot_accessories = ["Fan", "Water Bottle", "Sunscreen", "Parasol", "Sunglasses"]
        hot_bottoms = ["Short Skirt", "Cargo Shorts", "Jean Shorts", "Trackpants", "Athletic Shorts"]

        jackets = ["Jacket", "Parka", "Overcoat", "Jacket Shell", "Fur Coat", "Jean Jacket"]
        t_shirt = ["T-Shirt", "Tank Top", "Undershirt", "Polo"]
        long_sleeve_shirt = ["Long-Sleeve Shirt", "Light Sweatshirt", "Dress Shirt", "Blouse"]

        boots = ["Boots", "Hiking Boots", "Uggs", "Leather Shoes"]
        joggers = ["Running Shoes", "Slip-On Casual Shoes"]
        sandals = ["Slides", "Flip-Flops", "Sandals"]
        miscellanouse_shoes = ["Winter Moccasins", "Dress Shoes", "Heels"]

        full_length = ["Jeans", "Sweatpants", "Leggings", "Jeggings", "Khakis", "Long Skirt", "Cargo Pants", "Dress Pants", "Trackpants"]
        half_length = ["Short Skirt", "Cargo Shorts", "Jean Shorts", "Athletic Shorts"]

        weather = ["Thunderstorm", "Drizzle", "Rain", "Snow", "Atmosphere", "Clear", "Clouds"]


        return render_template('outfits.html', city = submitted_city, result = result, randomInt = random_num, coldFootwear = cold_footwear,
        coldBottoms = cold_bottoms, coldTop = cold_top, coldAccessories = cold_accessories,
        mildFootwear = mild_footwear, mildTop = mild_top, mildAccessories = mild_accessories, mildBottoms = mild_bottoms,
        hotFootwear = hot_footwear, hotTop = hot_top, hotAccessories = hot_accessories, hotBottoms = hot_bottoms, 
        jacketsIcon = jackets, tShirtIcon = t_shirt, longSleeveIcon = long_sleeve_shirt, bootsIcon = boots,
        joggersIcon = joggers, sandalsIcon = sandals, miscShoes = miscellanouse_shoes, halfBottomsIcon = half_length,
        fullBottomsIcon = full_length, weather = weather)



if __name__ == '__main__':
    app.run(debug=True)
