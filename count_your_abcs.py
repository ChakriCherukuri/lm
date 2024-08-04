def letter_count(x: str) -> dict:
    letter_counts = {}
    for letter in x.replace(" ", ""):
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts


n = int(input())

for i in range(n):
    print(max(letter_count(input()).values()))
