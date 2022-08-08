import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    d,x,y,z = [int(x) for x in input().split()]
    val = x*7
    val1 = y*d + (7-d)*z
    print(max(val,val1))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
