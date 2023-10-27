# Copyright © 2023, Indiana University
# BSD 3-Clause License

from flask import Flask, render_template
import csv

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")

def get_all_pets():
    '''Function to grab all pet data from the pets.csv file'''
    with open('pets.csv', encoding='UTF-8-sig') as csvfile:
        contents = csv.DictReader(csvfile)
        all_pets = {row['name']:{
            'name': row['name'],
            'description': row['description'],
            'details':[row['details_1'],row['details_2'],row['details_3']],
            'image_path': row['image_path'],
            'rating':row['rating']
            } for row in contents }
    return all_pets

@app.route('/')
@app.route('/pet')
@app.route('/pet/<pet_id>')
def index(pet_id=None):
    all_pets=get_all_pets()
    if pet_id and pet_id in all_pets.keys():
        return render_template('pet.html', pet=all_pets[pet_id])
    return render_template('index.html', pets=all_pets)

@app.route("/faq")
def faq_route():
    return render_template("faq.html")

@app.route("/about/")
def about_us():
    return render_template("about.html")

