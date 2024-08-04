import string

letter_counts = dict(zip(string.ascii_lowercase, range(1, 27)))

n = int(input())

result = []

for i in range(n):
    count = 0
    for letter in input():
        count += letter_counts[letter]
    print(count)
