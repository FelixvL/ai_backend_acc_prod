from flask import Blueprint, request
translate = Blueprint('translate', __name__)
import translateapp.translate_functions as translate_functions


@translate.route("/")
def start():
  translate_functions.a()
  return "translate endpoint v1"