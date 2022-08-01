import math


def answer_finder():
    n = int(input())
    print(math.ceil(n/4))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()