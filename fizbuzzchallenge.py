#!/usr/bin/env python3
#https://github.com/csfeeser/Python/blob/master/challenges/MODULO%20OPERATORS-%20fizzbuzz.md

for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:           
        print(x)
