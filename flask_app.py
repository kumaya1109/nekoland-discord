
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import requests
import os
from dotenv import load_dotenv
import json


load_dotenv(
    dotenv_path='.env',
    verbose=True
    )


DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)



@app.route("/discord", methods=["POST"])
def sendToDiscord():
    try:
        msg = request.form.get('message')
        secret = request.form.get('secret')

        if secret != SECRET_KEY:
            return 'authentication failed'

        content = {'content': msg}
        headers = {'Content-Type': 'application/json'}

        response = requests.post(DISCORD_WEBHOOK_URL, json.dumps(content), headers=headers)

        if response.status_code == requests.codes.ok or response.status_code == 204:
            return 'success'
        return 'failed status code: ' + str(response.status_code)

    except Exception as e:
        return 'server error reason: ' + e.message
