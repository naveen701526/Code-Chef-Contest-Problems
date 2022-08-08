import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y = [int(x) for x in input().split()]
    if x == y:
        print(0)
        return
    if y < x:
        val1 = x - y
        val = math.ceil(val1/2) if not val1%2 else math.ceil(val1/2) + 1
        
        
        
        print(val)
    else:
        print(y-x)



    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
