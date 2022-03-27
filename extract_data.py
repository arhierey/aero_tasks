def read_till_sep(string, sep):
    for index in range(0, len(string)):
        if string[index] == sep:
            res = string[0:index]
            return res
    return string


def graph_edge(one, another, container):
    if one == another:
        return 0
    for index in range(0, len(container)):
        if container[index][0] == one and container[index][1] == another:
            return 1
    return 0


def generic_search(vertex0, vertices, edges_arr):
    flags = [0]*len(edges_arr)
    explored = [vertex0]
    while not all(flags):
        size = len(explored)
        for index in range(0, len(edges_arr)):
            if edges_arr[index][0] in explored and edges_arr[index][1] not in explored:
                flags[index] = 1
                explored.append(edges_arr[index][1])
        if len(explored) == size:
            break
    result = [vertices[explored[index]] for index in range(0, len(explored))]
    return result


filename = 'api_output.txt'

with open(filename, 'r', encoding='utf-8') as file:
    output = file.read()

boards, boards0 = [], []
while output != '':
    data = read_till_sep(output, '$')
    length = len(data)

    while data != '':
        data0 = read_till_sep(data, ',')
        boards0.append(data0)
        data = data[len(data0)+1:len(data)+1]

    boards.append(boards0)
    output = output[length+1:len(output)+1]
    boards0 = []

dep_ports, arr_ports, ports = [], [], []
for i in range(0, len(boards)):
    if boards[i][0] not in dep_ports:
        dep_ports.append(boards[i][0])
    if boards[i][1] not in arr_ports:
        arr_ports.append(boards[i][1])
    if boards[i][0] not in ports:
        ports.append(boards[i][0])
    if boards[i][1] not in ports:
        ports.append(boards[i][1])

adj_matrix = [[graph_edge(ports[i], ports[j], boards) for i in range(0, len(ports))] for j in range(0, len(ports))]

edges = []
for i in range(0, len(ports)):
    for j in range(0, len(ports)):
        if adj_matrix[i][j] == 1:
            edges.append([i, j])

print(generic_search(5, ports, edges))
