n = int(input())

for i in range(n):
    v1, m1, v2, m2 = [float(i) for i in input().split(",")]
    result = (m1 * v1 + m2 * v2) / (m1 + m2)
    print(f"{result:.2f}")
