import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y = [int(x) for x in input().split()]
    val = math.floor((x+y)/2)
    print(max(abs(x-val), abs(y-val)))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
