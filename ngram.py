#!/usr/bin/env python3
""" n-gram challange module
"""
from collections import Counter


def calculateNGrams(text, n):
    """ Method that that given a piece of text and an integer n, it
        returns the n-grams for that text.
    """
    a = list(text)
    tmp = []
    for x in range(0, len(a)):
        new = a[x: n + x]
        m = ["".join(new)]
        if (len(new) == n):
            tmp.append(m)
            flat = [item for sublist in tmp for item in sublist]
    return flat

def mostFrequentNGram(text, n):
    """ Method that returns only the most
        frequent n-gram.
    """
    cal = calculateNGrams(text, n)
    cnt = Counter(cal)
    most = cnt.most_common(1)
    print(most[0][0]) 


print(calculateNGrams("to be or not to be", 2))
mostFrequentNGram("to be or not to be", 2)
