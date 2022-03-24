import requests as rq

url = 'http://api.aviationstack.com/v1/flights'
args = {'access_key': '***'}

res = rq.get(url, args)
response = res.json()
data = response['data']

some_data = dict(data[0])
keys = list(some_data.keys())

for key in keys:
    print(some_data[key])
