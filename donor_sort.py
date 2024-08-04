n = int(input())

for i in range(n):
    last_year_donors = set(input().split(","))
    current_donors = set(input().split(","))
    names = last_year_donors - current_donors
    print(",".join(sorted(names)))
    names_1 = last_year_donors & current_donors
    print((",".join(sorted(names_1))))
    names_2 = current_donors - last_year_donors
    print(",".join(sorted(names_2)))
