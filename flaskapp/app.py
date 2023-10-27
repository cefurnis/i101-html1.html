# Copyright © 2023, Indiana University
# BSD 3-Clause License

from flask import Flask, render_template, request, redirect, url_for
import csv
import operator 

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

# Events Route
@app.route("/events/", methods=['GET'])
def list_events():
    with open('Events.CSV') as csvfile:
               data = [row for row in csv.DictReader(csvfile)]
               data.sort(key=operator.itemgetter('event_date'))
               return render_template('events.html', events=data)
    

# Event Route
@app.route('/events/<event_id>', methods=['GET'])
def event(event_id = None, index=0):
        events= get_event()
        index= next((key for key, value in enumerate(events)if value['name_event']== event_id), None)
        return render_template('event.html', event = events, event_id = event_id, index = index)

# Venues Route
@app.route("/venues/", methods=['GET'])
def list_venues():
    with open('Venues.CSV') as csvfile:
               data = [row for row in csv.DictReader(csvfile)]
               data.sort(key=operator.itemgetter('rental_fee'))
               return render_template('venues.html', venues=data)

# People Route
@app.route("/people/", methods=['GET'])
def list_people():
        with open('People.CSV') as csvfile:
               data = [row for row in csv.DictReader(csvfile)]
               data.sort(key=operator.itemgetter('birth_date'))
        return render_template('people.html', people=data)


def get_event():
    with open('Events.CSV', encoding="UTF-8-sig") as csvfile:
        data = csv.DictReader(csvfile)
        events = []
        for row in data:
            events.append(row)
    return events
            