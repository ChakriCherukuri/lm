n = int(input())

for i in range(n):
    ip_address = input()
    if len(ip_address) == 0 or ip_address[0] == "." or ip_address[-1] == ".":
        print("INVALID")
    else:
        new_ip = [int(i) for i in ip_address.split(".")]
        min_ip = min(new_ip)
        max_ip = max(new_ip)
        if len(new_ip) == 4 and min_ip >= 0 and max_ip <= 255:
            print("VALID")
        else:
            print("INVALID")
