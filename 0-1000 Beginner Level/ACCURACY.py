import math


def answer_finder():
    x = int(input())
    val = math.ceil(x/3)
    if val*3 - x == 0:
        print(0)
    else:
        print(val*3-x)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()