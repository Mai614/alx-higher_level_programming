#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i), end="")
    print(chr(i - (i % 32)), end="")
