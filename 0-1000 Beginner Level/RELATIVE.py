import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')
import math


def answer_finder():
    k, n , w = [int(x) for x in input().split()]
    facts = (w*(w+1))/2
    val = k*facts
    ans = val - n if (val -n) > 0 else 0
    ans = math.ceil(ans)
    print(ans)
    


answer_finder()