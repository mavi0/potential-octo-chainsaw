import requests
res = requests.post('http://localhost:5000/api/get_message/1234', json={"mytext":"lalala"})
if res.ok:
    print res.json()