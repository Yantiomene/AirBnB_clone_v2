#!/usr/bin/python3
""" File to start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_session(exception):
    """Teardown"""
    storage.close()


@app.route("/hbnb")
def hbnb():
    """function  to render the state, cities, places and amenities"""
    return render_template('100-hbnb.html',
                           places=storage.all(Place).values(),
                           amenities=storage.all(Amenity).values(),
                           states=storage.all(State).values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
