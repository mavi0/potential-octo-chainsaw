from flask import Flask, request, jsonify
from config import HOSTS

import hashlib

app = Flask(__name__)

hosts_uuid = []

def gen_uuids(hosts):
    for host in hosts:
        hosts_uuid.append(hashlib.md5(host.encode('utf-8')).hexdigest())

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
@app.route('/api/get_message/<uuid>', methods=['GET'])


def get_message(uuid):
    content = "MESSAGE"
    return jsonify({"content":content})

def add_message(uuid):
    content = request.json
    print(content)
    return jsonify({"uuid":uuid})


if __name__ == '__main__':
    gen_uuids(HOSTS)
    app.run(host= '0.0.0.0',debug=True)