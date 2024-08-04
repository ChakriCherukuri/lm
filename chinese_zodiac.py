n = int(input())

elements = {0: "Wood", 1: "Fire", 2: "Earth", 3: "Metal", 4: "Water"}

animals = {
    0: "Rat",
    1: "Ox",
    2: "Tiger",
    3: "Rabbit",
    4: "Dragon",
    5: "Snake",
    6: "Horse",
    7: "Goat",
    8: "Monkey",
    9: "Rooster",
    10: "Dog",
    11: "Pig",
}

for i in range(n):
    result = []
    year = int(input())

    result.append(str(year))
    if year % 2 == 0:
        result.append("Yang")
    else:
        result.append("Yin")
    result.append(elements[int(((year - 4) % 10) / 2)])
    result.append(animals[(year - 4) % 12])
    print(" ".join(result))
