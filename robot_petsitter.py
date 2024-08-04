n = int(input())

for i in range(n):
    origin = [0, 0]
    for x in input():
        if x == "L":
            origin[0] -= 1
        elif x == "R":
            origin[0] += 1
        elif x == "U":
            origin[1] += 1
        elif x == "D":
            origin[1] -= 1
    if origin[0] == 0 and origin[1] == 0:
        print("TRUE")
    else:
        print("FALSE")
