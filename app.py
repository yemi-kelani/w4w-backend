from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

@app.route('/wakeup')
def wake_up():
    return 'Backend is awake!!'

@app.route('/besttime', methods=["POST"])
def besttime():
    BESTTIME_PRI_APIKEY = os.getenv('BESTTIME_PRI_APIKEY')
    input_json = request.get_json(force=True) 
    url = "https://besttime.app/api/v1/forecasts"

    params = {
        'api_key_private': BESTTIME_PRI_APIKEY,
        'venue_name': input_json['name'],
        'venue_address': input_json['location']
    }

    response = requests.request("POST", url, params=params)
    return jsonify(response.json())