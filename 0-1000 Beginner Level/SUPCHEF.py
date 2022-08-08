import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    m,n,k=[int(x) for x in input().split()]
    val = n*k
    if val < m:
        print('Yes')
    else:
        print('No')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
