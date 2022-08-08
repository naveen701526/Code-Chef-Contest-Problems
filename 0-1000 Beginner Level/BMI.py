import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    m,h = [int(x) for x in input().split()]
    val = m / pow(h,2)
    if val <= 18:
        print(1)
    elif val > 18 and val <= 24:
        print(2)
    elif val > 24 and val <= 29:
        print(3)
    else:
        print(4)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
