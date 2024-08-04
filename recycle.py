n = int(input())

for i in range(n):
    tokens = [int(i) for i in input().split()]
    a, b, c = tokens
    new_a = (a * 31) * 0.05
    new_b = (b * 15) * 0.10
    new_c = (c / 2) * 0.20

    result = new_a + new_b + new_c
    print(f"${result:.2f}")
