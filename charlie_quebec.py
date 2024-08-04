def convert_code(s: str) -> str:
    return "-".join([alphabet_map[letter] for letter in s])


n = int(input())

alphabet_map = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
}

for i in range(n):
    m = int(input())
    for j in range(m):
        s = input().upper()
        words = s.split()
        converted_words = [convert_code(word) for word in words]
        print(" ".join(converted_words))
