from collections import OrderedDict

n = int(input())

file_map = OrderedDict()

for i in range(n):
    token = input().split(".")[1]
    if token not in file_map:
        file_map[token] = 1
    else:
        file_map[token] += 1

for k, v in file_map.items():
    print(k, v)
