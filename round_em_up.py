n = int(input())

for i in range(n):
    tokens = [int(i) for i in input().split()]
    for token in tokens:
        if token % 2 != 0:
            tokens[tokens.index(token)] += 1
        else:
            tokens[tokens.index(token)] += 2
    print(" ".join([str(token) for token in tokens]))
