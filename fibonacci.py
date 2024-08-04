fibs = {
    1: 0,
    2: 1,
}

n = int(input())

for i in range(n):
    m = int(input())
    if m in fibs:
        print(f"{m} = {fibs[m]}")
    else:
        for i in range(3, m + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        print(f"{m} = {fibs[m]}")
