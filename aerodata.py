import requests as rq


def get_key(filename):
    with open(filename, 'r') as file:
        output = file.read()
    return output


url = 'http://api.aviationstack.com/v1/flights'
args = {'access_key': get_key('KEY.txt')}

res = rq.get(url, args)
response = res.json()
data = response['data']

with open('api_output.txt', 'w') as f:
    for i in range(0, len(data)):
        f.write("%s\n" % data[i])
