import math


def answer_finder():
    n,k,m = [int(x) for x in input().split()]
    c = k*m
    print(math.ceil(n/c))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()