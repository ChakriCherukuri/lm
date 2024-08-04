n = int(input())

for i in range(n):
    s, classification = input().split()
    first = s[:3]
    second = s[3:6]
    third = s[6:]
    numbers = [first, second, third]
    if classification == "DASHES":
        print("-".join(numbers))
    elif classification == "PERIODS":
        print(".".join(numbers))
    elif classification == "PARENTHESES":
        print(f"({first}) {second}-{third}")
