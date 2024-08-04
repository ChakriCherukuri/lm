n = int(input())

for i in range(n):
    new_inputs = input().split()
    if new_inputs[0] == new_inputs[1]:
        print("true")
    else:
        print("false")
