"""
    This script is aim to init data for this specific DataSource.
"""
import os
import json
import requests

HOSTNAME = 'http://127.0.0.1:10001/api/v0.1'

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

RESOURCE_PATH = os.path.join(ABS_PATH,'data/data.json')

login_user = {
    'username': 'testuser',
    'password': 'Hello'
}

print 'user login'
req = requests.post(HOSTNAME+'/auth', json=login_user)
if not req.__bool__():
    print 'failed login'
d = req.json()
ext_id = d['ext_id']
print json.dumps(d, indent=4)


with open(RESOURCE_PATH) as f:
    data = json.loads(f.read())

for d in data:
    req = requests.post(HOSTNAME+'/data', json=d, headers={'Authorization': 'Bearer ' + ext_id})

    if not req.__bool__():
        print 'failed create categories'

    resp = req.json()
    print json.dumps(resp, indent=4)