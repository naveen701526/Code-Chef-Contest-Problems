import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n,x,k = [int(x) for x in input().split()]
    print(k//x if k//x <= n else n )
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
