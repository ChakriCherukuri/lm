n = int(input())

for i in range(n):
    tokens = [int(token) for token in input().split(", ")]
    a, b, c = tokens
    if a + b <= c or b + c <= a or a + c <= b:
        print("Not a Triangle")
    else:
        if len(set(tokens)) == 3:
            print("Scalene")
        elif len(set(tokens)) == 2:
            print("Isosceles")
        elif len(set(tokens)) == 1:
            print("Equilateral")
