import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b,m = [int(x) for x in input().split()]
    val = abs(a-b)
    val1 = m - val
    print(min(val,val1))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
