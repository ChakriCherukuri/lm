n = int(input())

for i in range(n):
    m = int(input())
    for i in range(m):
        a, b, c = [i[0].upper() for i in input().split()]
        print(f"{a}{c}{b}")
