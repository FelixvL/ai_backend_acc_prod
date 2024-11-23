from flask import Blueprint, request
adventure = Blueprint('adventure', __name__)
import adventure_travelapp.adventure_travel_functions as af


@adventure.route("/")
def start():
  adventure_functions.a()
  return "adventure endpoint v1"


@adventure.route("/startscript")
def startscript():
  return af.startscript()

