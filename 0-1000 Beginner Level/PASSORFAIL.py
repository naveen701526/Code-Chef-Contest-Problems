import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n,x,p = [int(x) for x in input().split()]
    score = x*3 - (n-x)
    if score >= p:
        print('PASS')
    else:
        print('FAIL')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
