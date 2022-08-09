import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    q, p = [int(x) for x in input().split()]
    if q > 1000:
        res = 0.9*p*q
        print('{:.6f}'.format(res))
    else:
        res = p*q
        print('{:.6f}'.format(res))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
