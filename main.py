#! /usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

sms_webhook_path_secret = app.config.from_envvar('SMS_WEBHOOK_PATH')
@app.route(f'/sms_receive/{sms_webhook_path_secret}')
def receive_sms_webhook():
    return 'This path receives the SMSes'
