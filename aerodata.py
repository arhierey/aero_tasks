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

keys = list(data[0].keys())

boards = []
for i in range(0, len(data)):
    dep_port = data[i]['departure']['airport']
    arr_port = data[i]['arrival']['airport']
    dep_time = data[i]['departure']['scheduled']
    arr_time = data[i]['arrival']['scheduled']
    dep_zone = data[i]['departure']['timezone']
    arr_zone = data[i]['arrival']['timezone']

    with open('api_output.txt', 'a', encoding='utf-8') as f:
        csv_str = '{},{},{},{},{},{}$'.format(dep_port, arr_port, dep_time, arr_time, dep_zone, arr_zone)
        f.write(csv_str)
