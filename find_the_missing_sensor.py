n = int(input())

for i in range(n):
    m = int(input())
    nums = [int(token) for token in input().split()]
    sorted_nums = list(range(1, m + 1))
    for s in sorted_nums:
        if s not in nums:
            print(s)
