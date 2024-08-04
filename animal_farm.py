n = int(input())

for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    print(a * 2 + b * 4 + c * 4)
