n = int(input())


def get_letter_counts(s: str) -> dict[str, int]:
    letter_counts = {}
    for letter in s:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts


def is_same_letters(s1: dict, s2: dict) -> bool:
    for k, v in s1.items():
        if k not in s2:
            return False
        elif s1[k] != s2[k]:
            return False
    return True


for i in range(n):
    letter1, letter2 = input().split()
    letter_1 = get_letter_counts(letter1)
    letter_2 = get_letter_counts(letter2)
    if not is_same_letters(letter_1, letter_2):
        print(letter1)
    elif letter1[0] == letter2[0] and letter1[-1] == letter2[-1]:
        print(letter2)
    else:
        print(letter1)
