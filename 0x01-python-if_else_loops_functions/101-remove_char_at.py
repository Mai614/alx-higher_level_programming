#!/usr/bin/python3

def remove_char_at(letter, n):
    if n < 0:
        return (letter)
    return (letter[:n] + letter[n+1:])
