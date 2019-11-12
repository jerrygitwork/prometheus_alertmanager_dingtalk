# coding: utf-8
import base64
import hmac
import hashlib
import json
import os
import requests
import sys
import time
import urllib

from flask import Flask
from flask import request
from oslo_config import cfg
from oslo_log import log

import config
import opts

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_data()
        alerts = get_alerts(json.loads(data))
        for alert in alerts:
            send_alert(generate_sendData(alert))
        return 'Successfully send message to dingtalk.'
    else:
        return 'please post alerts'

def generate_sendData(alert):
    sendData = {
        "msgtype": "text",
        "text": {
            "content": alert
        }
    }
    return sendData

def get_alerts(data):
    alerts = []
    for alert in data['alerts']:
        if len(alert):
            alerts.append(alert_format(alert))
    return alerts

def alert_format(alert):
    message = u'【%s %s】告警状态: %s, 告警级别: %s, 告警时间: %s, 告警描述: %s,\
        告警建议: %s' % (alert['labels']['alertname'],
        alert['status'], alert['status'], alert['labels']['severity'], alert['startsAt'],
        alert['annotations']['description'], alert['annotations']['suggestion'])

    if alert['status'] == 'firing':
        return message
    if alert['status'] == 'resolved':
        return message + u'结束时间: ' + alert['endsAt']

def generate_signature(secret):
    timestamp = long(round(time.time() * 1000))
    secret_enc = bytes(secret).encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign

def send_alert(data):
    conf = cfg.CONF
    timestamp, sign = generate_signature(conf.dingtalk.secret)
    url = '%s&timestamp=%s&sign=%s' %(conf.dingtalk.token_url, timestamp, sign)
    req = requests.post(url, json=data)
    result = req.json()
    if result['errcode'] != 0:
        print('%s: failed send alerts to dingtalk.' % result['errcode'])

def main():
    config.parse_args(sys.argv)
    opts.register_opts()
    conf = cfg.CONF
    app.run(host=conf.server.addr, port=conf.server.port)

if __name__ == '__main__':
    main()
