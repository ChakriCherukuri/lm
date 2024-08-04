bat_map = {"K": 0, "1B": 1, "2B": 2, "3B": 3, "HR": 4}
n = int(input())
for i in range(n):
    s = input()
    name, characters = s.split(":")
    at_bats = [token for token in characters.split(",") if token != "BB"]
    if len(at_bats) == 0:
        result = 0
    else:
        result = sum([bat_map[a] for a in at_bats]) / len(at_bats)
    print(f"{name}={result:.3f}")
