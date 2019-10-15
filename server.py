from flask import Flask, request, jsonify, make_response
from config import HOSTS

import hashlib, json

app = Flask(__name__)

hosts_uuid = []

def gen_uuids(hosts):
    for host in hosts:
        hosts_uuid.append(hashlib.md5(host.encode('utf-8')).hexdigest())
    print(hosts_uuid)


@app.route('/api/get_stats/<uuid>', methods=['GET'])
def get_stats(uuid):
    content = "MESSAGE"
    return jsonify({"content":content})

@app.route('/api/set_stats/<uuid>', methods=['GET', 'POST'])
def set_stats(uuid):
    for host_uuid in hosts_uuid:
        if uuid == host_uuid:
            with open(uuid + '.json', 'w') as f:
                json.dump(request.json, f)
            return make_response("OK", 200)
    
    return make_response("UUID Not Found", 404)


if __name__ == '__main__':
    gen_uuids(HOSTS)
    app.run(host= '0.0.0.0',debug=True)