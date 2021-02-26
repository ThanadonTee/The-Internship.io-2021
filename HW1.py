#!/usr/bin/env python3

out = []
for i in range(int(input())):
    acronyms = ""
    tmp = [word for word in input().split(" ") if not word.islower() and not word.isupper()]
    for i in tmp:
        acronyms += i[0]
    out.append(acronyms)
out.sort(key=len, reverse=True)
for i in out:
    print(i)