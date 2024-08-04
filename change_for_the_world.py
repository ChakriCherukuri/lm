n = int(input())

result = []

for i in range(n):
    s = input()
    new_s = s.replace("$", "")
    n = int(float(new_s) * 100)

    Q = n // 25
    n = n % 25
    D = n // 10
    n = n % 10
    N = n // 5
    n = n % 5
    P = n

    print(s)
    print(f"Quarters={Q}")
    print(f"Dimes={D}")
    print(f"Nickels={N}")
    print(f"Pennies={P}")
