#!/usr/bin/env python3
""" n-gram challange module
"""


def calculateNGrams(text, n):
    """ Method that that given a piece of text and an integer n, it
        returns the n-grams for that text.
    """
    a = list(text)
    for x in range(0, len(a)):
        new = a[x: n + x]
        if (len(new) == n):
            strs = ""
            list(new)
            lists = strs.join(new)
            print(lists, end=" ")

calculateNGrams("Slang", 2)

