#!/usr/bin/env python3

def prime(number: int) -> bool:
    if (number <= 1) : 
        return False
    if (number <= 3) : 
        return True
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

def floatPrime(number: float) -> bool:
    if number > 10 or number < 1:
        return False
    for i in range(3):
        number *= 10
        if prime(int(number)):
            return True
    return False

while True:
    tmp = float(input())
    if tmp == 0.0 :
        break
    print(floatPrime(tmp))