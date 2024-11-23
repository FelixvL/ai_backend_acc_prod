from flask import Flask
from flask_cors import CORS

from blueprints.translate_ep import translate
from blueprints.adventure_travel_ep import adventure

app = Flask(__name__)
CORS(app)

app.register_blueprint(translate, url_prefix='/translate')
app.register_blueprint(adventure, url_prefix='/adventure')

@app.route("/")
def helloWorld():
  return "Hello, Versie 3!"