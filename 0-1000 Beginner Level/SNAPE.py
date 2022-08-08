import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    b, ls = [int(x) for x in input().split()]
    rs_min = pow(ls,2) - pow(b,2)
    rs_min = math.sqrt(rs_min)
    rs_max = pow(ls,2) + pow(b,2)
    rs_max = math.sqrt(rs_max)
    print(round(rs_min,5), end=' ')
    print(round(rs_max,5))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
