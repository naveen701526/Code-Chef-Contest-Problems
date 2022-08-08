import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    xa, xb, Xa, Xb = [int(x) for x in input().split()]
    val1 = math.ceil(Xa/xa)
    val2 = math.ceil(Xb/xb)
    print(val1+val2)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
