import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y = [int(x) for x in input().split()]
    val = math.ceil(y/10)
    val1 = math.ceil(x/10)
    
    res = abs(val - val1)
    print(res if res != 0 else 0)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
