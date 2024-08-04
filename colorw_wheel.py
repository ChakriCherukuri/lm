n = int(input())

for i in range(n):
    color = input()
    primary_colors = ["red", "blue", "yellow"]
    if color not in primary_colors:
        if color == "violet":
            print(f"In order to make violet, blue and red must be mixed.")
        if color == "green":
            print(f"In order to make green, blue and yellow must be mixed.")
        if color == "orange":
            print(f"In order to make orange, red and yellow must be mixed.")
        if color == "red-orange":
            print(f"In order to make red-orange, red and yellow must be mixed.")
        if color == "yellow-orange":
            print(f"In order to make yellow-orange, red and yellow must be mixed.")
        if color == "yellow-green":
            print(f"In order to make yellow-green, blue and yellow must be mixed.")
        if color == "blue-green":
            print(f"In order to make blue-green, blue and yellow must be mixed.")
        if color == "blue-violet":
            print(f"In order to make blue-violet, blue and red must be mixed.")
        if color == "red-violet":
            print(f"In order to make violet, blue and red must be mixed.")
    else:
        print(f"No colors need to be mixed to make {color}.")
