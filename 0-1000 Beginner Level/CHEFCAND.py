import math


def answer_finder():
    n, x = [int(x) for x in input().split()]
    val = n-x
    if val < 0:
        print(0)
    else:
        ans = math.ceil(val/4)
        print(ans)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()