n = int(input())

for i in range(n):
    tokens = sorted([int(i) for i in input().split(",")])
    print(",".join([str(token) for token in tokens]))
