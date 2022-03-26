def read_till_sep(string, sep):
    for i in range(0, len(string)):
        if string[i] == sep:
            res = string[0:i]
            return res
    return string


filename = 'api_output.txt'

with open(filename, 'r', encoding='utf-8') as file:
    output = file.read()

data_list, data_list0 = [], []
while output != '':
    data = read_till_sep(output, '$')
    length = len(data)

    while data != '':
        data0 = read_till_sep(data, ',')
        data_list0.append(data0)
        data = data[len(data0)+1:len(data)+1]

    data_list.append(data_list0)
    output = output[length+1:len(output)+1]
    data_list0 = []

dep_ports, arr_ports = [], []
for i in range(0, len(data_list)):
    if data_list[i][0] not in dep_ports:
        dep_ports.append(data_list[i][0])
    if data_list[i][1] not in arr_ports:
        arr_ports.append(data_list[i][1])
