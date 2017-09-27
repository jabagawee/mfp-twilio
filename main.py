#! /usr/bin/env python

import os

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route(f'/sms_receive/{os.environ["SMS_WEBHOOK_PATH"]}')
def receive_sms_webhook():
    return 'This path receives the SMSes'
