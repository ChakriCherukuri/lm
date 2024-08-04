n = int(input())

for i in range(n):
    m = int(input())
    for j in range(m):
        num = int(input())
        if num < 1582:
            print("No")
        elif num % 4 != 0:
            print("No")
        else:
            print("Yes")
