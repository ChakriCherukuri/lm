n = int(input())

for i in range(n):
    m = int(input())
    for i in range(m):
        s = input()
        link, kilobytes = s.split()
        if not link.endswith(".lmco.com") and int(kilobytes) > 1000:
            print(s)
