import math
# import sys
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    x, y = [int(x) for x in input().split()]
    if x == y:
        print(0)
    else:
        val = y - x
        req = math.ceil(val/8)
        print(req)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
