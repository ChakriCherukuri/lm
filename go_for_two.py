n = int(input())

for i in range(n):
    a, b = [int(i) for i in input().split()]
    if (
        b - 15 == a
        or b - 13 == a
        or b - 11 == a
        or b - 10 == a
        or b - 8 == a
        or b - 5 == a
        or b - 4 == a
        or b - 2 == a
    ):
        print(2)
    elif (
        b - 14 == a
        or b - 12 == a
        or b - 9 == a
        or b - 7 == a
        or b - 6 == a
        or b - 3 == a
        or b - 1 == a
    ):
        print(1)
    elif b + 1 == a or b + 5 == a or b + 1 == a or b + 12 == a:
        print(2)
    else:
        print(1)
