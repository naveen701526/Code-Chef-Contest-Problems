import math
# import sys
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    x,y,z = [int(x) for x in input().split()]
    val = math.ceil(y/x)
    print(z-val if z- val >= 0 else 0)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
