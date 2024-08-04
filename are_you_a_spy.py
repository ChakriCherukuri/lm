import string


def check_contains(s1, s2) -> bool:
    for letter in s2:
        if letter not in s1:
            return False
    return True


n = int(input())

for i in range(n):
    s1, s2 = input().split("|")
    s1_clean = [letter for letter in s1.lower() if letter in string.ascii_lowercase]
    s2_clean = [letter for letter in s2.lower() if letter in string.ascii_lowercase]
    if check_contains(s1_clean, s2_clean):
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")
