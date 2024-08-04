import sys


def hamming_distance(str1: str, str2: str):
    if len(str1) != len(str2):
        return float("inf")
    else:
        distance = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
    return distance


n = int(input())

dict_words = []

for i in range(n):
    x, y = [int(i) for i in input().split()]
    for j in range(x):
        dict_words.append(input())
    for m in range(y):
        w = input()
        hd_list = [hamming_distance(word, w) for word in dict_words]
        min_h = min(hd_list)
        print(dict_words[hd_list.index(min_h)])
