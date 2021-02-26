#!/usr/bin/env python3

ansList = ["_","_","_","_","_","_","_","_","_","_","_","_",""]
key = input().split(" ")
for i in range(5):
    guess = input()
    if guess in key:
        for j in range(12):
            if guess == key[j]:
                ansList[j] = guess
    else:
        ansList[12] += guess + " "
    print("".join(ansList))
print(12-ansList.count("_"))