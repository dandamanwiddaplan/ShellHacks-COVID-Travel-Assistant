#If you see this, then I did something right.
import datetime
import json
import os
import binascii

import dialogflow
import pusher
import requests
from flask import Flask, jsonify, render_template, request
from google.api_core.exceptions import InvalidArgument

from query import query

app = Flask(__name__)

# DIALOGFLOW_PROJECT_ID = 'covidtravelassistant'
# DIALOGFLOW_LANGUAGE_CODE = 'en-US'
# GOOGLE_APPLICATION_CREDENTIALS = 'static\JSON\covidtravelassistant-7fccee1a19f5.json'
# SESSION_ID =  [ session for session in range(0,99999) ]
# text_to_be_analyzed = "Hi! I'm David and I'd like to eat some sushi, can you help me?"
# session_client = dialogflow.SessionsClient()
# session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
# text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
# query_input = dialogflow.types.QueryInput(text=text_input)
# try:
#     response = session_client.detect_intent(session=session, query_input=query_input)
# except InvalidArgument:
#     raise
# print("Query text:", response.query_result.query_text)
# print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# print("Fulfillment text:", response.query_result.fulfillment_text)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def send():
    req = request.json
    destination = req['destination']
    date = datetime.datetime.strptime(req['date'], '%Y-%m-%d')
    print(destination)
    print(date)
    
    #Perform a query.
    QUERY = (
        'SELECT * FROM `bigquery-public-data.covid19_public_forecasts.county_14d` '
        f'WHERE state_name = "{destination}" '
        'AND prediction_date > forecast_date '
        'ORDER BY prediction_date '
        'LIMIT 100')

    result = clean_query(QUERY)
    return jsonify(result)
    
# POST example template
# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     new_records = []
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#     for r in records:
#         if r['name'] == record['name']:
#             r['email'] = record['email']
#         new_records.append(r)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(new_records, indent=2))
#     return jsonify(record)


if __name__ == "__main__":
    app.run(debug=True, port=80)